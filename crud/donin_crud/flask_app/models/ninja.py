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
        self.dojo_id = data['dojo_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(fname)s, %(lname)s, %(age)s, NOW(), NOW());"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def clear(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name=%(fname)s, last_name=%(lname)s, age=%(age)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])