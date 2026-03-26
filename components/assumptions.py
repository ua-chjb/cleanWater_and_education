from dash_iconify import DashIconify
import dash_mantine_components as dmc

from components.accordion import full_accordion
from utils.assumptions_text import assumptions_pf_dct, assumptions_text_dct
from utils.colors import colors


def assumptions_accordion():

    return dmc.Accordion(
        [
            full_accordion(
                id=key.lower().replace(" ", "-"),
                header=key,
                text={0: val},
                pf=assumptions_pf_dct[key],
            )
            for key, val in assumptions_text_dct.items()
        ],
        id="assumptions_accordion_IN",
    )
