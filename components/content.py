from dash import html
import dash_mantine_components as dmc

from pages.intro import intro
from pages.eda import eda
from pages.geo import geo
from pages.assumptions import assumptions
from pages.model import model

content_map = {
    "nav-intro": intro,
    "nav-eda": eda,
    "nav-geo": geo,
    "nav-assumptions": assumptions,
    "nav-model": model,
}

headers_map = {
    "nav-intro": dmc.Text("Introduction", size="md", fw=300, c="white"),
    "nav-eda": dmc.Text("EDA", size="md", fw=300, c="white"),
    "nav-geo": dmc.Text("Map", size="md", fw=300, c="white"),
    "nav-assumptions": dmc.Text("OLS assumptions", size="md", fw=300, c="white"),
    "nav-model": dmc.Text("Model", size="md", fw=300, c="white"),
}
