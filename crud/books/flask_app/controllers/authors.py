from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def author_dashboard():
    authors = Author.get_all()
    return render_template('dashboard.html', authors = authors)

@app.route('/process/create_author', methods=['POST'])
def create():
    Author.save(request.form)
    return redirect('/authors')