from dash import html
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from utils.colors import colors

color = colors["white"]

icon_github = DashIconify(
    icon="simple-icons:github", width=30, color=color, className="bb"
)
link_github = "https://www.github.com/ua-chjb"
icon_linkedin = DashIconify(
    icon="devicon-plain:linkedin", width=30, color=color, className="bb"
)
link_linkedin = "https://linkedin.com/in/benjaminbnoyes"
icon_email = DashIconify(icon="mdi:email", width=30, color=color, className="bb")
link_email = "mailto:noyesbenjamin@gmail.com"
icon_spotify = DashIconify(icon="cib:spotify", width=30, color=color, className="bb")
link_spotify = (
    "https://open.spotify.com/playlist/2s1oHEgwqxVKoqNdOC1Zs4?si=17fbc35fb4c9421c"
)
icon_soundcloud = DashIconify(
    icon="cib:soundcloud", width=40, color=color, className="bb"
)
link_soundcloud = "https://soundcloud.com/bennoyes-onb"


comp20_footer0_github = dmc.Anchor(
    icon_github,
    href=link_github,
    target="_blank",
    size="xl",
    className="footnt-child comp20_footer0_github",
)

comp21_footer1_linkedin = dmc.Anchor(
    icon_linkedin,
    href=link_linkedin,
    target="_blank",
    size="xl",
    className="footnt-child comp21_footer1_linkedin",
)

comp22_footer2_email = dmc.Anchor(
    icon_email,
    href=link_email,
    target="_blank",
    size="sm",
    className="footnt-child comp22_footer2_email",
)

comp23_footer3_spotify = dmc.Anchor(
    icon_spotify,
    href=link_spotify,
    target="_blank",
    size="xl",
    className="footnt-child comp23_footer3_spotify",
)

comp24_footer4_soundcloud = dmc.Anchor(
    icon_soundcloud,
    href=link_soundcloud,
    target="_blank",
    size="xl",
    className="footnt-child comp24_footer4_soundcloud",
)

comp25_copyrightfooter = html.P(
    "© Benjamin Noyes 2026 all rights reserved", className="footertinytext"
)

comp27_github_parent = html.Div([comp20_footer0_github], className="footnt-parent")
comp28_linkedin_parent = html.Div([comp21_footer1_linkedin], className="footnt-parent")
comp29_email_parent = html.Div([comp22_footer2_email], className="footnt-parent")
comp30_spotify_parent = html.Div([comp23_footer3_spotify], className="footnt-parent")
comp31_soundcloud_parent = html.Div(
    [comp24_footer4_soundcloud], className="footnt-parent"
)

comp26_icons = html.Div(
    [
        comp27_github_parent,
        comp28_linkedin_parent,
        comp29_email_parent,
        comp30_spotify_parent,
        comp31_soundcloud_parent,
    ],
    className="footie-middle",
)


footer = html.Div(
    [comp26_icons, comp25_copyrightfooter],
    className="footie-all",
)
