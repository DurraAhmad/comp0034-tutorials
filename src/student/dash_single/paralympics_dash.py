# Imports for Dash and Dash.html
from dash import Dash, html
# Import for bootstrap CSS
import dash_bootstrap_components as dbc

# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external CSS to use 
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Create an instance of the Dash app
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Structuring
row_one = dbc.Row([
    dbc.Col([
        html.H1('Paralympics Data Analytics'),
        html.P('This dashboard provides insights into Paralympics data.'),
    ],)
])

row_two = dbc.Row([
    dbc.Col(children=[
        dbc.Select(
            options=[
                {'label': 'Events', 'value': 'events'},
                {'label': 'Sports', 'value': 'athletes'},
                {'label': 'Countries', 'value': 'countries'},
                {'label': 'Athletes', 'value': 'participants'},
            ],
            value='events', # default value
            id='dropdown-input',
        )
    ], width = 4),
    dbc.Col(children=[
        html.Div(
            [
                dbc.Label("Select the Paralympic Games type"),
                dbc.Checklist(
                    options=[
                        {'label':'Summer', 'value':'summer'},
                        {'label':'Winter', 'value':'winter'},
                    ],
                    value=['summer'],
                    id='checklist-input',
                ),
            ]
        )
    ], width={"size": 4, "offset": 2}),
])

row_three = dbc.Row([
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('line-chart-placeholder.png'),
                 className='img-fluid'),
    ], width = 6),
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('bar-chart-placeholder.png'),
                className='img-fluid'),
    ], width = 6),
])

row_four = dbc.Row([
    dbc.Col(children=[
        html.Img(src=app.get_asset_url('map-placeholder.png'),
                className='img-fluid'),
    ], width = 8),
    dbc.Col(children=[
        dbc.Card([
            dbc.CardImg(src=app.get_asset_url('logos/2022_Beijing.jpg'), top=True),
            dbc.CardBody([
                html.H4("Beijing 2022", className="card-title"),
                html.P("Number of athletes: XX", className="card-text", ),
                html.P("Number of events: XX", className="card-text", ),
                html.P("Number of countries: XX", className="card-text", ),
                html.P("Number of sports: XX", className="card-text", ),
            ]),
        ])
    ], style={"width": "18rem"}),
])

# Add an HTML layout to the Dash app
app.layout = dbc.Container([
    # The layout will go here
    row_one,
    row_two,
    row_three,
    row_four,
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
