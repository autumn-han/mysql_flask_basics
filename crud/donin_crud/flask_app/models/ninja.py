from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, NOW(), NOW());"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    