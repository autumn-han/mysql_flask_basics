from mysqlconnection import connectToMySQL

class User:
    DB = "users_cr"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id=%(id_num)s;"
        data = {"id_num": user_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL(cls.DB).query_db(query, data)