from dash import dcc, html
import dash_mantine_components as dmc

from utils.data import collst_fe, summ
from utils.eda_text import eda_text_dct

eda = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dmc.Card(
                            [
                                dmc.Text(t, size="sm", mb="sm")
                                for t in eda_text_dct.values()
                            ],
                            withBorder=True,
                            radius="md",
                            className="model-text-card",
                        ),
                        dmc.Card(
                            [
                                dmc.Select(
                                    id="eda_select_x_IN",
                                    label="x value",
                                    placeholder="Select...",
                                    data=collst_fe,
                                    value=collst_fe[1],
                                    clearable=False,
                                    searchable=True,
                                )
                            ],
                            radius="md",
                            withBorder=True,
                            className="eda-dropdown-card",
                        ),
                        dmc.Card(
                            [
                                dmc.Select(
                                    id="eda_select_y_IN",
                                    label="y value",
                                    placeholder="Select for scatter...",
                                    data=collst_fe,
                                    value=None,
                                    clearable=True,
                                    searchable=True,
                                )
                            ],
                            radius="md",
                            withBorder=True,
                            className="eda-dropdown-card",
                        ),
                        dmc.Card(
                            [
                                dmc.Select(
                                    id="eda_select_z_IN",
                                    label="z value",
                                    placeholder="select for scatter 3d...",
                                    data=collst_fe,
                                    value=None,
                                    clearable=True,
                                    searchable=True,
                                    disabled=True,
                                )
                            ],
                            radius="md",
                            withBorder=True,
                            className="eda-dropdown-card",
                        ),
                    ],
                    className="eda-dropdown-div in",
                ),
                dmc.Card(
                    [dcc.Graph(figure={}, id="eda_OUT")],
                    radius="md",
                    withBorder=True,
                    className="eda-graph-card",
                ),
            ],
            className="eda-fold-1",
        ),
        html.Div(
            [
                dmc.ScrollArea(
                    dmc.Table(
                        data={
                            "head": summ.drop(["index"], axis=1)
                            .astype(str)
                            .columns.tolist(),
                            "body": summ.drop(["index"], axis=1)
                            .astype(str)
                            .values.tolist(),
                        },
                        striped=True,
                        highlightOnHover=True,
                        withTableBorder=True,
                        withColumnBorders=True,
                    ),
                    type="auto",
                    className="eda-table",
                ),
            ],
            className="eda-fold-2",
        ),
    ]
)
