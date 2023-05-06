from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import order

class Customer:
    DB = "cookie_orders"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.orders = []

@classmethod
def all_customers(cls):
    query = "SELECT * FROM customers;"
    results = connectToMySQL(cls.DB).query_db(query)
    return results

@classmethod
def one_customer(cls, data):
    query = "SELECT * FROM orders JOIN customers ON orders.customer_id = orders.id WHERE customers.id = %(id)s;"
    results = connectToMySQL(cls.DB).query_db(query, data)
    customer = cls(results[0])
    for row in results:
        order_data = {
            "id": row["id"],
            "cookie_type": row["cookie_type"],
            "amount": row["amount"],
            "created_at": row["created_at"],
            "upated_at": row["updated_at"],
            "customer_id": row["customer_id"]
        }
        customer.orders.append(order.Order(order_data))
    return customer

@classmethod
def customer_info(cls, data):
    query = "SELECT * FROM customers WHERE id=%(id)s;"
    result = connectToMySQL(cls.DB).query_db(query, data)
    return cls(result[0])

