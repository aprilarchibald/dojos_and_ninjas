from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.models_dojos import Dojo
DATABASE ="dojos_and_ninjas"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name =data['last_name']
        self.age = data['age']
        # self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        user_id= connectToMySQL(DATABASE).query_db( query, data )
        return user_id 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            ninjas = []
            for ninja in results:
                ninjas.append(cls(ninja))
            return ninjas
        return []

    