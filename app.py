import boto3
from dash import Dash

from callbacks import switchboard
from index import Body

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = Body

switchboard(app)

server = app.server

if __name__ == "__main__":
    # app.run(debug=True, port="8050")  # for local development
    app.run(host="0.0.0.0", port=8050)  # for EC2 instance
