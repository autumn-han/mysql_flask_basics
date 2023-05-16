from flask_app import app
from flask import render_template
from flask_app.models.book import Book

@app.route('/books')
def all_books():
    books = Book.get_all()
    return render_template('books_dashboard.html', books = books)