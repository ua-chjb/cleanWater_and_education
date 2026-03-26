from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from utils.colors import colors


def accordion_control(header, pf=None):
    return dmc.AccordionControl(
        dmc.Group(
            [
                (
                    DashIconify(
                        icon=(
                            "mdi:check-circle" if pf == "Passed" else "mdi:close-circle"
                        ),
                        color=colors["green"] if pf == "Passed" else colors["red"],
                        width=20,
                    )
                    if pf
                    else None
                ),
                dmc.Text(header, size="xl", fw=700),
            ],
            gap="xs",
        )
    )


def accordion_panel(text):
    if isinstance(text, dict):
        return dmc.AccordionPanel(
            html.Div([dmc.Text(t, size="sm", mb="sm") for t in text.values()])
        )
    return dmc.AccordionPanel(text)


def full_accordion(id, header, text, pf=None):
    return html.Div(
        dmc.AccordionItem(
            [accordion_control(header, pf), accordion_panel(text)],
            value=id,
        ),
        className="methodology-accordion-item",
    )
