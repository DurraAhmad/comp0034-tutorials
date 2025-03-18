from dash import Dash
import dash_bootstrap_components as dbc
import dash

# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external CSS to use
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags, use_pages=True)

# Define navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Event Details", href=dash.page_registry['pages.events']['path'])),
        dbc.NavItem(dbc.NavLink("Charts", href=dash.page_registry['pages.charts']['path'])),
    ],
    brand="Paralympics Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
)

# Wrap the layout in a Bootstrap container
app.layout = dbc.Container([
    # Nav bar
    navbar, 
    # Area where the page content is displaed
    dash.page_container
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=9050)