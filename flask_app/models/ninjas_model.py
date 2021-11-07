# import the function that will return an instance of a connection ////////
from flask_app.config.mysqlconnection import connectToMySQL

TARGETDATABASE = 'dojos_and_ninjas_schema'                              # Designates the database we are using
TABLENAME = "ninjas"                                                     # Designates the table we are using

# //// NINJAS CLASS ////////////////////////////////////////////////////////
class Ninjas:
    def __init__( self , data ):                                        # Constructor function
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # //// CREATE //////////////////////////////////////////////////////////

    # **** Insert One Method ***********************************************
    # @returns ID of created user
    @classmethod
    def create(cls, data:dict ):
        query = "INSERT INTO " + TABLENAME +" (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(TARGETDATABASE).query_db( query, data )
        
    # //// RETRIEVE /////////////////////////////////////////////////////////

    # **** Get All Class Method *******************************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + TABLENAME + ";"
        results = connectToMySQL(TARGETDATABASE).query_db(query)        # Call the connectToMySQL function with the target db
        list_of_instances = []                                          # Initialize an empty list where we can store instances of the class
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            list_of_instances.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return list_of_instances
    
    # **** Get One Class Method *******************************************
    # @Returns: an instance of the class
    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM " + TABLENAME +" WHERE id = %(id)s;"
        results = connectToMySQL(TARGETDATABASE).query_db(query, data)  # Call the connectToMySQL function with the target db
                                                                        # result is a list of a single dictionary
        return cls(results[0])                                          # return an instance of the dictionary

    # //// UPDATE //////////////////////////////////////////////////////////

    # **** Update One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def update_one(cls, data:dict):
        query = "UPDATE " + TABLENAME +" SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s WHERE id=%(id)s"
        return connectToMySQL(TARGETDATABASE).query_db(query, data)

    # //// DELETE //////////////////////////////////////////////////////////

    # **** Delete One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def delete(cls, data:dict):
        query = "DELETE FROM " + TABLENAME + " WHERE id=%(id)s"
        return connectToMySQL(TARGETDATABASE).query_db(query, data)