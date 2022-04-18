from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_ninjas


DATABASE = "dojos_and_ninjas"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # @property
    # def fullname(self):
    #     return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
    
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        user_id= connectToMySQL(DATABASE).query_db( query, data )
        return user_id 


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            dojos = []
            for dojo in results:
                dojos.append(cls(dojo))
            return dojos
        return []

    @classmethod
    def get_one(cls,data:dict):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result= connectToMySQL(DATABASE).query_db( query, data )
        if result:
            return cls(result[0])
        return False
        

    
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        ninja_id_result = connectToMySQL(DATABASE).query_db( query, data )
        dojos = cls(ninja_id_result[0])
        for ninja in ninja_id_result:

            ninja_data= {
                # **request.form,
                # "id":id

                "id": ninja['ninjas.id'], 
                "first_name": ninja["first_name"],
                "last_name": ninja["last_name"],
                "age": ninja["age"],
                "created_at": ninja["ninjas.created_at"],
                "updated_at": ninja["ninjas.updated_at"],
            }
            dojos.ninjas.append(models_ninjas.Ninja(ninja_data))
        return dojos