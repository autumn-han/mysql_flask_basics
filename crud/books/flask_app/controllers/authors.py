from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.author import Author
from flask_app.models.book import Book

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
    data = {
        "id": id
    }
    author = Author.get_one(data)
    auth = Author.get_by_authid(data)
    books = Book.get_all()
    return render_template('one_author.html', author = author, auth = auth, books = books)

@app.route('/process/add_fave_book', methods=['POST'])
def save_fave():
    Book.save_fave(request.form)
    return redirect(url_for('show_author', id = request.form["user_id"]))