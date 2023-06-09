from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    DB = "cookie_orders"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.boxes = data["boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def all_orders(cls):
        query = "SELECT * FROM cookie_orders;"
        results = connectToMySQL(cls.DB).query_db(query)
        return results
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookie_orders (name, cookie_type, boxes, created_at, updated_at) VALUES (%(name)s, %(cookie_type)s, %(boxes)s, NOW(), NOW());"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def update(cls, data):
        query = "UPDATE cookie_orders SET name=%(name)s, cookie_type=%(cookie_type)s, boxes=%(boxes)s, updated_at=NOW() WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def one_order(cls, data):
        query = "SELECT * FROM cookie_orders WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @staticmethod
    def validate_user(order):
        is_valid = True
        if len(order["name"]) <= 2:
            flash("Customer name must be attached to order")
            is_valid = False
        if len(order["cookie_type"]) <= 2:
            flash("Must state what type of cookie is being ordered")
            is_valid = False
        if int(order["boxes"]) <= 0:
            flash("Number of boxes must be at least 1")
            is_valid = False
        return is_valid