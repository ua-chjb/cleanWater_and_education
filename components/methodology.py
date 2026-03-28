import dash_mantine_components as dmc

from components.accordion import full_accordion
from utils.methodology_text import methodology_text_dct

methodology_accordion = dmc.Accordion(
    [
        full_accordion(id=key.lower().replace(" ", "-"), header=key, text=val)
        for key, val in methodology_text_dct.items()
    ],
    className="methodology-accordion",
    value="informal-hypothesis",
)
