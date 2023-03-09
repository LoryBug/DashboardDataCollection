import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
server = app.server