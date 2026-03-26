from dash import html, dcc, _dash_renderer
from dash_iconify import DashIconify
import dash_mantine_components as dmc

_dash_renderer._set_react_version("18.2.0")

from pages.intro import intro
from components.cards import top_cards
from components.footer import footer
from components.header import header
from components.mobile import mobile

Header = html.Div(
    [
        mobile,
        header,
        html.Div(
            [
                top_cards,
                html.Div(
                    id="main-content",
                    children=intro,
                ),
                dcc.Location(id="url", refresh=True),
                dcc.Store(id="active-page", data="overview"),
            ],
            className="desktop-only",
        ),
        footer,
    ]
)

Body = dmc.MantineProvider(
    [
        Header,
    ]
)
