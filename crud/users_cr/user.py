from mysqlconnection import connectToMySQL

class Friend:
    DB = "first_flask"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, num):
        query = "SELECT * FROM friends WHERE id = %(num)s;"
        data = {'id': num}
        result = connectToMySQL(cls.DB).query_db(query)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
    @classmethod
    def save(cls, data):
        query = """INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result