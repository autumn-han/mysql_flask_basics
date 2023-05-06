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
def all_orders(cls):
    # work on method definition here #
