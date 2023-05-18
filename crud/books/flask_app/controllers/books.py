from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def all_books():
    books = Book.get_all()
    return render_template('books_dashboard.html', books = books)

@app.route('/process/add_book', methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    book = Book.get_one(data)
    books = Book.get_by_bookid(data)
    authors = Author.get_all()
    return render_template('one_book.html', book = book, books = books, authors = authors)

@app.route('/process/add_fave_book', methods=['POST'])
def save_fave_auth():
    Book.save_fave(request.form)
    return redirect(url_for('show_book', id = request.form["book_id"]))

