# all the pages layout


import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from app import app

###################################################
# STYle css da portare poi in file separato
###################################################
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#353f61"
}


###################################################
# DEFINE REUSABLE COMPONENTS AS FUNCTION
###################################################

# function
# Header with logo
def get_header():

    header = html.Div([

        # Same as img width, allowing to have the title centrally aligned
        html.Div([], className='col-2'),

        html.Div([
            html.H1(children='Data Collection Dashboard',
                    style={'textAlign': 'center'}
                    )],
                 className='col-8',
                 style={'padding-top': '1%'}
                 ),

        html.Div([
            html.Img(
                src=app.get_asset_url('logo.png'),
                height='43 px',
                width='auto')
        ],
            className='col-2',
            style={
            'align-items': 'center',
            'padding-top': '1%',
            'height': 'auto'})

    ],
        className='row',
        style={'height': '4%'}
    )

    return header


def get_sidebar():
    sidebar = html.Div(
        [
            html.H2("Dashboard", className="display-4"),
            html.Hr(),
            html.P(
                "Data collection scripts", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink("Overview", href="/apps/overview",
                                active="exact"),
                    dbc.NavLink("Run Scripts",
                                href="/apps/run_script", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar


def get_navbar():
    navbar = html.Div(
        [
            dbc.NavbarSimple(
                children=[
                    dbc.NavLink("Overview", href="/apps/overview", active="exact"),
                    dbc.NavLink("Run Scripts", href="/apps/run_script", active="exact"),
                ],
                brand="Navbar with active links",
                color="primary",
                dark=True,
            ),
            dbc.Container(id="page-content", className="pt-4"),
        ]
    )
    return navbar

###################################################
# OVERVIEW PAGE LAYOUT
###################################################
overview_page = html.Div([
    html.P("overview")
])


###################################################
# RUN PAGE LAYOUT
###################################################


# SSH part
ssh_div = html.Div()

# SNMP part
snmp_div = html.Div()


runScript_page = html.Div([
     get_navbar(),
    html.P("Run")
]
   
)

