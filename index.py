# navigation file
from dash import dcc
from dash import html
import dash

from app import app
from app import server
from page_layouts import overview_page, runScript_page
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return overview_page
    elif pathname == '/apps/run_script':
         return runScript_page
    else:
        return overview_page # This is the "home page"

if __name__ == '__main__':
    app.run_server(debug=True)