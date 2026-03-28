import dash_mantine_components as dmc

from components.card import card
from utils.colors import colors

top_cards = dmc.Group(
    [
        card(84, "countries", colors["blue"]),
        card(11, "initial predictors", colors["blue"]),
        card(4, "final predictors", colors["blue"]),
        card(0.231, "final model r2", colors["blue"]),
    ],
    className="intro-lyt",
    gap="xs",
)
