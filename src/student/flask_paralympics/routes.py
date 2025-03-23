""" This is an example of a minimal Flask application."""
# Import the Flask class from the Flask library
from flask import Blueprint, render_template

# define a Blueprint
main = Blueprint('main', __name__)


# Add a route for the 'home' page
# use the route() decorator to tell Flask what URL should trigger our function.
@main.route('/')
def home():
    # Default route for the base URL
    return render_template('index.html', name='World')
@main.route('/<name>')
def index(name):
    # The function returns the message we want to display in the user’s browser. The default content type is HTML,
    # so HTML in the string will be rendered by the browser.
    return render_template('index.html', name=name)

# A route that uses a template to generate the page
# @app.route('/hello')
# def hello_with_template():
#     # The function renders a template that generates the home page using HTML
#     return render_template('hello.html')