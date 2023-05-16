from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(fname)s, %(lname)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result