from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dojo_name)s, NOW(), NOW());"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result