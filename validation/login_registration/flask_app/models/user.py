from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "login_registration"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s);"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(User.DB).query_db(query, user)
        if len(result) >= 1:
            flash("email is already linked to another account, please enter a different email")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("invalid email address")
            is_valid = False
        if str.isalpha(user["fname"]) == False: 
            flash("first name cannot contain numbers") 
            is_valid = False
        if len(user["fname"]) < 2:
            flash("first name must be at least 2 letters")
            is_valid = False
        if str.isalpha(user["lname"]) == False:
            flash("last name cannot contain numbers")
            is_valid = False
        if len(user["lname"]) < 2:
            flash("last name must be at least 2 letters")
            is_valid = False
        if len(user["password"]) < 8:
            flash("password must be at least 8 characters")
            is_valid = False
        if user["password"] != user["confirm"]:
            flash("password entries do not match with each other")
            is_valid = False
        return is_valid
    

        

