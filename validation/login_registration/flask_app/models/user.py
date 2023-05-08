from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

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
    def save(cls):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s);"
        result = connectToMySQL(cls.DB).query_db(query)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        email_present = cls(result[0])
        return email_present
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if str.isalpha(user["fname"]) == False: 
            flash("first name cannot contain numbers")
            # could maybe add first name and last name string checks together 
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
        if not EMAIL_REGEX.match(user["email"]):
            flash("invalid email address")
            is_valid = False
        if User.get_by_email(user["email"]) == True:
            is_valid = False
        if len(user["password"]) < 8:
            flash("password must be at least 8 characters")
            is_valid = False
        

