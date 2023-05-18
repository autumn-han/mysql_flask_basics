from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VAlUES (%(title)s, %(pages)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def save_fave(cls, data):
        query = "INSERT INTO favorites (book_id, user_id) VALUES (%(book_id)s, %(user_id)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_by_bookid(cls, data):
        query = "SELECT * FROM users JOIN favorites ON users.id = favorites.user_id JOIN books ON favorites.book_id = books.id WHERE books.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        book = cls(results[0])
        for row in results:
            author_info = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            book.authors.append(author.Author(author_info))
        return book
    
    