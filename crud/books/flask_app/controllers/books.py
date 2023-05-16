from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book import Book

@app.route('/books')
def all_books():
    books = Book.get_all()
    return render_template('books_dashboard.html', books = books)

@app.route('/process/add_book', methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

