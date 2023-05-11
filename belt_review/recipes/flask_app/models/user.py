from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.recipe import Recipe
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE users.id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_user_recipes(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE users.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        user = cls(results[0])
        for row in results:
            recipe = {
                "id": row["id"],
                "name": row["name"],
                "description": row["description"],
                "instructions": row["instructions"],
                "date_made": row["date_made"],
                "under": row["under"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "user_id": row["user_id"]
            }
            user.recipes.append(Recipe(recipe))
        return user

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(User.DB).query_db(query, user)
        if len(result) >= 1:
            flash("email is already linked to another account, please enter a different email", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("invalid email address", "registration")
            is_valid = False
        if str.isalpha(user["fname"]) == False: 
            flash("first name cannot contain numbers", "registration") 
            is_valid = False
        if len(user["fname"]) < 2:
            flash("first name must be at least 2 letters", "registration")
            is_valid = False
        if str.isalpha(user["lname"]) == False:
            flash("last name cannot contain numbers", "registration")
            is_valid = False
        if len(user["lname"]) < 2:
            flash("last name must be at least 2 letters", "registration")
            is_valid = False
        if len(user["password"]) < 8:
            flash("password must be at least 8 characters", "registration")
            is_valid = False
        if user["password"] != user["confirm"]:
            flash("password entries do not match with each other", "registration")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form):
        if not EMAIL_REGEX.match(form["email"]):
            flash("invalid email address", "login")
            return False
        user = User.get_by_email(form)
        if not user:
            flash("username does not exist", "login")
            return False
        if not bcrypt.check_password_hash(user.password, form["password"]):
            flash("wrong password", "login")
            return False
        return user
    
    
        
    

