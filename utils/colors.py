import plotly.express as px

from utils.data import we

colors = {
    "blue": "#228be6",
    "gray": "gray",
    "green": "#2b8a3e",
    "red": "#c92a2a",
    "white": "white",
}

color_lst = px.colors.qualitative.Prism
unique_countries_lst = we["country"].unique()
color_map_dct = {
    country: color_lst[j % len(color_lst)]
    for j, country in enumerate(unique_countries_lst)
}
