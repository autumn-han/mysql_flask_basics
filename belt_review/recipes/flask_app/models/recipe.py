from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    DB = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under = data["under"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, date_made, under) VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL(cls.DB).query_db(query)
        return results
    
