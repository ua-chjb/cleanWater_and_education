from dash import ctx, dcc, Input, Output, State
import plotly.graph_objects as go

from components.layout import lyt
from components.charts import (
    assumptions_homoskedasticity,
    assumptions_linearity,
    assumptions_multicollinearity,
    assumptions_normality_of_residuals,
    histogram_or_scatter,
    map_geo,
)
from components.content import content_map, headers_map
from utils.data import sm_model, sm_resids, sm_Y_preds


def switchboard(app):

    @app.callback(
        Output("drawer_OUT", "opened"),
        Input("drawer_IN", "n_clicks"),
        State("drawer_OUT", "opened"),
        prevent_initial_call=True,
    )
    def all_drawer_usestate(n_clicks, opened):
        return True

    @app.callback(
        Output("main-content", "children"),
        Output("header_OUT", "children"),
        Output("drawer_OUT", "opened", allow_duplicate=True),
        Output("active-page", "data"),
        Input("nav-intro", "n_clicks"),
        Input("nav-eda", "n_clicks"),
        Input("nav-geo", "n_clicks"),
        Input("nav-assumptions", "n_clicks"),
        Input("nav-model", "n_clicks"),
        prevent_initial_call=True,
    )
    def all_navigate(intro, eda, geo, assumptions, model):
        triggered_id = ctx.triggered_id
        content = content_map.get(triggered_id, content_map["nav-intro"])
        header = headers_map.get(triggered_id, headers_map["nav-intro"])
        page_id = triggered_id.replace("nav-", "") if triggered_id else "intro"
        return content, header, False, page_id

    @app.callback(
        Output("main-content", "children", allow_duplicate=True),
        Output("header_OUT", "children", allow_duplicate=True),
        Output("active-page", "data", allow_duplicate=True),
        Input("home_button_IN", "n_clicks"),
        prevent_initial_call=True,
    )
    def all_home_affix(n_clicks):
        return (content_map["nav-intro"], headers_map["nav-intro"], "intro")

    @app.callback(
        Output("eda_OUT", "figure"),
        Input("eda_select_x_IN", "value"),
        Input("eda_select_y_IN", "value"),
    )
    def eda_fold_one(x, y):
        return lyt(histogram_or_scatter(x, y))

    @app.callback(
        Output("map_OUT", "figure"),
        Input("map_select_IN", "value"),
    )
    def map_geo_color(x):
        return lyt(map_geo(x))

    @app.callback(
        Output("assumptions_graph_OUT", "figure"),
        Output("assumptions_graph_OUT", "style"),
        Output("assumptions_table_OUT", "children"),
        Output("assumptions_card_OUT", "style"),
        Input("assumptions_accordion_IN", "value"),
    )
    def update_assumptions_graph(value):

        hide_graph = {"display": "none"}
        show_graph = {"display": "block"}
        hide_card = {"display": "none"}
        show_card = {"display": "block"}

        if value is None or value == "independence-of-observations":
            return go.Figure(), hide_graph, None, hide_card

        elif value == "linearity":
            return (
                lyt(assumptions_linearity(sm_model, sm_Y_preds, sm_resids)),
                show_graph,
                None,
                show_card,
            )

        elif value == "homoskedasticity":
            return (
                lyt(assumptions_homoskedasticity(sm_model, sm_resids, sm_Y_preds)),
                show_graph,
                None,
                show_card,
            )

        elif value == "normality-of-residuals":
            return (
                lyt(assumptions_normality_of_residuals(sm_resids)),
                show_graph,
                None,
                show_card,
            )

        elif value == "no-perfect-multicollinearity":
            return go.Figure(), hide_graph, assumptions_multicollinearity(), show_card

        return go.Figure(), hide_graph, None, hide_card
