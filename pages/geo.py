from dash import dcc, html
import dash_mantine_components as dmc

from components.charts import map_geo

from utils.data import collst_fe

geo = html.Div(
    [
        html.Div(
            [
                dmc.Card(
                    [
                        dmc.Select(
                            id="map_select_IN",
                            label="color value",
                            placeholder="Select...",
                            data=collst_fe + ["population"],
                            value="population",
                            clearable=False,
                            searchable=True,
                        )
                    ],
                    withBorder=True,
                    radius="md",
                    className="map-dropdown",
                ),
            ],
            className="in",
        ),
        dmc.Card(
            [dcc.Graph(figure={}, id="map_OUT", style={"height": "100%"})],
            withBorder=True,
            radius="md",
            className="map-graph",
        ),
    ],
    className="map-fold-1",
)
