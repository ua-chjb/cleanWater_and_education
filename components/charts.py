import dash_mantine_components as dmc
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, linear_rainbow

from utils.colors import colors, color_map_dct
from utils.data import vif_df, we, sm_sf_preds
from utils.geojson import geojson


def map_geo(x):
    if x in ["lower_school_water__none", "lower_school_water__limited"]:
        colorscale = "balance"
    elif x in ["population"]:
        colorscale = "Emrld"
    else:
        colorscale = "balance_r"
    return (
        px.choropleth_mapbox(
            we,
            geojson=geojson,
            featureidkey="properties.ISO_A2",
            locations="iso_a2",
            color=x,
            hover_data={
                "country": True,
                x: ":.1f",
                "college_enrollment": ":.1f",
            },
            color_continuous_scale=colorscale,
            mapbox_style="carto-positron",
            opacity=0.8,
            zoom=2,
            center={"lat": 20, "lon": 0},
        )
        .update_traces(marker_line_width=1, marker_line_color="#cccccc")
        .update_layout({"title": {"text": f"{x} by country"}})
    )


def histogram_or_scatter(x, y=None):

    fig = go.Figure()

    if y == None:
        return fig.add_trace(
            go.Histogram(x=we[x], marker={"color": colors["blue"]})
        ).update_layout({"title": {"text": f"Distribution of {x}"}})
    else:
        m, b = np.polyfit(we[x], we[y], deg=1)
        x_line = np.linspace(we[x].min(), we[x].max(), 100)
        y_line = m * x_line + b

        return (
            fig.add_trace(
                go.Scattergl(
                    x=we[x],
                    y=we[y],
                    showlegend=False,
                    mode="markers",
                    marker={
                        "color": colors["blue"],
                    },
                    name=f"{x} by {y}",
                ),
            )
            .add_trace(
                go.Scatter(
                    x=x_line,
                    y=y_line,
                    mode="lines",
                    showlegend=False,
                    line={"color": "gray", "dash": "dash"},
                    name=f"OLS",
                ),
            )
            .update_layout(
                {
                    "title": {"text": f"{x} by {y}"},
                    "xaxis": {"title": {"text": f"{x}"}},
                    "yaxis": {"title": {"text": f"{y}"}},
                }
            )
        )


def assumptions_linearity(sm_model, sm_Y_preds, sm_resids):
    stat, pvalue = linear_rainbow(sm_model)

    result = "failed" if pvalue < 0.05 else "passed"

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=sm_Y_preds,
            y=sm_resids,
            mode="markers",
            name="residuals",
            marker={"color": "#228be6"},
        )
    ).update_layout(
        {
            "title": f"Linear Rainbow test {result}: statistic={stat:.4f}, p-value={pvalue:.4f}",
            "xaxis": {"title": "predictions"},
            "yaxis": {"title": "residuals"},
        }
    )

    return fig


def assumptions_homoskedasticity(sm_model, sm_resids, sm_Y_preds):

    bp_stat, bp_p, f_stat, f_p = het_breuschpagan(sm_model.resid, sm_model.model.exog)

    result = "failed" if f_p < 0.05 else "passed"

    sqrt_abs_resids = np.sqrt(np.abs(sm_resids))

    lowess_res = sm.nonparametric.lowess(sqrt_abs_resids, sm_Y_preds, frac=0.6)
    lowess_x = lowess_res[:, 0]
    lowess_y = lowess_res[:, 1]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=sm_Y_preds,
            y=sqrt_abs_resids,
            mode="markers",
            name="residuals",
            marker={"color": "#228be6"},
        )
    ).add_trace(
        go.Scatter(
            x=lowess_x,
            y=lowess_y,
            mode="lines",
            name="LOWESS",
            line={"color": "red", "dash": "dash"},
        )
    )

    return fig.update_layout(
        {
            "title": {
                "text": f"Het Breusch-Pagan test {result}: statistic= {f_stat:.4f}, p-val={f_p:.4f}"
            },
            "xaxis": {"title": {"text": "predictions"}},
            "yaxis": {
                "title": {"text": "square root of the absolute value of the residuals"}
            },
        }
    )


def assumptions_normality_of_residuals(sm_resids):
    (theoretical_q, sample_q), (slope, intercept, r) = stats.probplot(sm_resids)

    line_x = np.array([min(theoretical_q), max(theoretical_q)])
    line_y = slope * line_x + intercept

    stat, pvalue = stats.shapiro(sm_resids)
    result = "passed" if pvalue > 0.05 else "failed"
    title_text = f"Shapiro-Wilk {result}: statistic={stat:.4f}, pvalue={pvalue:.4f}"

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=theoretical_q,
            y=sample_q,
            mode="markers",
            name="residuals",
            marker={"color": "#228be6"},
        )
    ).add_trace(
        go.Scatter(
            x=line_x,
            y=line_y,
            mode="lines",
            name="normal reference",
            line={"color": "red", "dash": "dash"},
        )
    ).update_layout(
        {
            "title": {"text": title_text},
            "xaxis": {"title": {"text": "theoretical quantiles of residuals"}},
            "yaxis": {"title": {"text": "sample quantiles of residuals"}},
        }
    )

    return fig


def assumptions_multicollinearity():
    vif_df["VIF"] = vif_df["VIF"].round(4)

    return dmc.Table(
        data={"head": vif_df.columns.tolist(), "body": vif_df.values.tolist()},
        striped=True,
        highlightOnHover=True,
        withTableBorder=True,
        withColumnBorders=True,
    )


def conf_pred_interval_scatter(ols=True):

    x = "lower_school_water__none"
    y = "college_enrollment"

    sort_idx = we[x].argsort()
    df_sorted = we.iloc[sort_idx]
    sf_sorted = sm_sf_preds.iloc[sort_idx]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_sorted[x],
            y=df_sorted[y],
            hovertext=df_sorted["country"],
            mode="markers",
            showlegend=False,
            marker={
                "size": df_sorted["population1"],
                "color": [color_map_dct[c] for c in df_sorted["country"]],
            },
            name="% no access to water",
        )
    )

    if ols:
        fig.add_trace(
            go.Scatter(
                x=df_sorted[x],
                y=sf_sorted["mean"],
                mode="lines",
                line={"color": "gray", "dash": "dash"},
                name="Predictions",
            )
        ).add_trace(
            go.Scatter(
                x=df_sorted[x],
                y=sf_sorted["obs_ci_upper"],
                mode="lines",
                line={"width": 0},
                showlegend=False,
            )
        ).add_trace(
            go.Scatter(
                x=df_sorted[x],
                y=sf_sorted["obs_ci_lower"],
                mode="lines",
                line={"width": 0},
                fill="tonexty",
                fillcolor="rgba(100,149,237,0.15)",
                name="Prediction interval (95%)",
            )
        ).add_trace(
            go.Scatter(
                x=df_sorted[x],
                y=sf_sorted["mean_ci_upper"],
                mode="lines",
                line={"width": 0},
                showlegend=False,
            )
        ).add_trace(
            go.Scatter(
                x=df_sorted[x],
                y=sf_sorted["mean_ci_lower"],
                mode="lines",
                line={"width": 0},
                fill="tonexty",
                fillcolor="rgba(100,149,237,0.35)",
                name="Confidence interval (95%)",
            )
        )
    return fig.update_layout(
        {
            "title": {
                "text": "The more lower schools have no access to water, the lower college education rates"
            },
            "xaxis": {"title": {"text": f"{x}"}},
            "yaxis": {"title": {"text": f"{y}"}},
        }
    )
