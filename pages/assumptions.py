from dash import dcc, html
import dash_mantine_components as dmc

from components.assumptions import assumptions_accordion
from utils.assumptions_text import assumptions_summ_text

assumptions = html.Div(
    [
        html.Div(
            [
                dmc.Card(
                    [dmc.Text(assumptions_summ_text, size="sm")],
                    withBorder=True,
                    radius="md",
                    className="assumptions-left-top",
                ),
                dmc.Card(
                    [
                        dcc.Graph(id="assumptions_graph_OUT"),
                        html.Div(id="assumptions_table_OUT"),
                    ],
                    withBorder=True,
                    radius="md",
                    id="assumptions_card_OUT",
                    className="assumptions-left-bottom",
                ),
            ],
            className="assumptions-left in",
        ),
        html.Div(
            [assumptions_accordion()],
            className="assumptions-right",
        ),
    ],
    className="assumptions-fold-1",
)
