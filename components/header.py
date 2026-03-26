from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from components.nav import Nav


header = html.Div(
    [
        html.Div(
            [
                dmc.ActionIcon(
                    DashIconify(icon="mingcute:menu-fill", width=20),
                    variant="filled",
                    color="blue",
                    id="drawer_IN",
                    className="nav-hamburger",
                ),
                dmc.Drawer(children=Nav, title="Menu", id="drawer_OUT", padding="md"),
            ],
            className="header-nav",
        ),
        html.Div(
            [
                dmc.Title(
                    "Clean Water and Education, by Country",
                    order=1,
                    className="header-text",
                ),
                html.Div(
                    dmc.Text("Introduction", size="md", fw=300, c="white"),
                    id="header_OUT",
                    className="header-page-title",
                ),
            ],
            className="header-text-div",
        ),
    ],
    className="header-main-div",
)
