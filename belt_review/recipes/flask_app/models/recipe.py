from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

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
    def get_one(cls, data): 
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        return results
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under=%(under)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 3:
            flash("recipe name must be at least 3 characters", "recipe")
            is_valid = False
        if len(recipe["description"]) < 3:
            flash("recipe description must be at least 3 characters", "recipe")
            is_valid = False
        if len(recipe["instructions"]) < 3:
            flash("recipe instructions must be at least 3 characters", "recipe")
            is_valid = False
        if recipe["date_made"] == "":
            flash("please mark a date", "recipe")
            is_valid = False
        if "under" not in recipe:
            flash("please check either yes or no", "recipe")
            is_valid = False
        return is_valid
