""" This is an example of a minimal Flask application."""
# Import the Flask class from the Flask library
from flask import Blueprint, render_template
from student.flask_paralympics.db import get_db
import sqlite3

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

@main.route('/events')
def get_events():
    db = get_db()
    events = db.execute('SELECT * FROM Event').fetchall()
    events_text = [f'{event["year"]} {event["type"]} {event["start"]} {event["end"]}' for event in events]
    return events_text

@main.route('/add-quiz-data')
def add_sample_quiz_data():
    db = get_db()
    try:
        # Insert the data, uses hard coded values for now
        quiz = db.execute('INSERT INTO quiz (quiz_name) VALUES (?)', ('Sample Quiz',))
        question = db.execute('INSERT INTO question (question) VALUES (?)',
                              ('What year were the paralympics first held in Barcelona?',))
        db.execute('INSERT INTO quiz_question (quiz_id, question_id) VALUES (?, ?)',
                   (quiz.lastrowid, question.lastrowid))
        db.execute('INSERT INTO answer_choice (question_id, choice_text, choice_value, is_correct) VALUES (?, ?, ?, ?)',
                   (question.lastrowid, '1992', 5, 1))
        # Commit the changes made above
        db.commit()
        return 'Sample data added to the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)

# Add a route to save a student response to the quiz
@main.route('/save-response')
def save_student_response():
    db = get_db()
    try:
        # Insert the data, uses hard coded values for now
        student_response = db.execute(
            'INSERT INTO student_response (student_email) VALUES (?)', ('sample@email.com',))
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)

# Add a route to update the close date of a quiz
@main.route('/update-quiz/<quiz_id>/<close_date>')
def update_quiz(quiz_id, close_date):
    db = get_db()
    try:
        db.execute('UPDATE quiz SET close_date = ? WHERE quiz_id = ?', (close_date, quiz_id))
        db.commit()
        return 'Quiz updated in the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)
    
# Add a route to delete the student response using the id
@main.route('/update-quiz/<quiz_id>/<close_date>')
def update_quiz(quiz_id, close_date):
    db = get_db()
    try:
        db.execute('UPDATE quiz SET close_date = ? WHERE quiz_id = ?', (close_date, quiz_id))
        db.commit()
        return 'Quiz updated in the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)
