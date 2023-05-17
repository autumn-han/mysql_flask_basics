from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
# from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def author_dashboard():
    authors = Author.get_all()
    return render_template('dashboard.html', authors = authors)

@app.route('/process/add_author', methods=['POST'])
def create():
    Author.save(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    author = Author.get_one(id)
    fave_books = Author.get_by_authid(id)
    return render_template('one_author.html', author = author, fave_books = fave_books)