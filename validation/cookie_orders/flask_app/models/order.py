from flask_app.config.mysqlconnection import connectToMySQL

class Order:
    DB = "cookie_orders"
    def __init__(self, data):
        self.id = data["id"]
        self.cookie_type = data["cookie_type"]
        self.amount = data["amount"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.customer_id = data["customer_id"]
    
    @classmethod
    def one_order(cls, data):
        query = "SELECT * FROM orders WHERE orders.id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def all_orders(cls):
        query = "SELECT orders.id, orders.cookie_type, orders.amount, customers.name FROM orders JOIN customers ON orders.customer_id = orders.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        return results
    
    @classmethod
    def update(cls, data):
        query = """UPDATE orders 
        SET orders.cookie_type=%(cookie_type)s, orders.amount=%(amount)s, orders.updated_at=NOW() 
        FROM orders JOIN customers ON orders.customer_id = customers.id
        WHERE orders.id=%(id)s;"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
