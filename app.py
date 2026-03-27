from dash import Dash

from callbacks import switchboard
from index import Body

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = Body

switchboard(app)

server = app.server
