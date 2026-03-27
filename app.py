from dash import Dash

from callbacks import switchboard
from index import Content

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = Content

switchboard(app)

server = app.server
