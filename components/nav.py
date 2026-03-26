import dash_mantine_components as dmc

Nav = dmc.Stack(
    [
        dmc.NavLink(label="Introduction", id="nav-intro"),
        dmc.NavLink(label="EDA", id="nav-eda"),
        dmc.NavLink(label="Map", id="nav-geo"),
        dmc.NavLink(label="OLS Assumptions", id="nav-assumptions"),
        dmc.NavLink(label="Model", id="nav-model"),
    ]
)
