from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []

@classmethod
def create(cls, data):
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s);"
    result = connectToMySQL(cls.DB).query_db(query, data)
    return result
