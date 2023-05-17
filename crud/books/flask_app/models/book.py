from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VAlUES (%(title)s, %(pages)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    