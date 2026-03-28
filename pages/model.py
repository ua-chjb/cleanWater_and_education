from dash import dcc, html
import dash_mantine_components as dmc

from components.charts import conf_pred_interval_scatter
from components.df_to_table import to_dmc_table
from utils.data import tables
from utils.model_text import model_text_dct

model = html.Div(
    [
        html.Div(
            [
                dmc.Card(
                    [dmc.Text(t, size="sm", mb="sm") for t in model_text_dct.values()],
                    withBorder=True,
                    radius="md",
                    className="model-text-card",
                ),
                dmc.Select(
                    id="model-summ-IN",
                    label="model summaries",
                    placeholder="select...",
                    data=["Model overview", "Coefficients", "Diagnostics"],
                    value="Model overview",
                    clearable=False,
                    searchable=True,
                    disabled=False,
                ),
            ],
            className="model-left in",
        ),
        html.Div(
            [
                dmc.Card(
                    [dcc.Graph(figure=conf_pred_interval_scatter())],
                    withBorder=True,
                    radius="md",
                    className="model-graph-card",
                ),
                html.Div(
                    [
                        dmc.Card(
                            [],
                            id="model-summ-OUT",
                            withBorder=True,
                            radius="md",
                            className="model-table-card",
                        ),
                    ],
                    className="model-right-bottom",
                ),
            ],
            className="model-right",
        ),
    ],
    className="model-fold-1",
)
