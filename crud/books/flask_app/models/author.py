from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.fave_books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(fname)s, %(lname)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_by_authid(cls, data):
        query = "SELECT * FROM books JOIN favorites ON books.id = favorites.book_id JOIN users ON favorites.user_id = users.id WHERE users.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        author = cls(results[0])
        for row in results:
            book_info = {
                "id": row["id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            author.fave_books.append(book.Book(book_info))
        return author
    
