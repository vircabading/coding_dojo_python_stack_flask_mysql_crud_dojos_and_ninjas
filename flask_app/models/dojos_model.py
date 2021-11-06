# import the function that will return an instance of a connection ////////
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninjas_model

TARGETDATABASE = 'dojos_and_ninjas_schema'                              # Designates the database we are using
TABLENAME = "dojos"                                                     # Designates the table we are using

# //// DOJOS CLASS //////////////////////////////////////////////////////////
class Dojos:
    def __init__( self , data ):                                        # Constructor function
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []                                                # Create empty list to hold instances of ninjas in the dojo

    # //// CREATE //////////////////////////////////////////////////////////

    # **** Insert One Method ***********************************************
    # @returns ID of created user
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO " + TABLENAME +" (name) VALUES ( %(name)s );"
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

    # **** JOIN ACION ******************************************************
    # **** Get One Dojo with All its Ninjas ********************************
    # @returns: an instance of the dojo
    @classmethod
    def get_dojo_with_ninjas (cls, data:dict):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        print("**** Query ********************************")
        print(query)
        print("Data:")
        print(data)
        results = connectToMySQL(TARGETDATABASE).query_db(query, data)        # Call the connectToMySQL function with the target db
                                                                        # results is a list of dictionaries
        
        print("***********************************************")
        print("In get Dojo with Ninjas")
        print("***********************************************")
        print(results)

        dojo = cls(results[0])                                          # get an instance of this dojo

        for row_from_db in results:                                     # loop through all the list of dictionaries
            ninja_data = {                                                  # use the dictionaries we are loopimg through to build a data structure
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninjas_model.Ninjas(ninja_data))        # get an instance of a ninja and append it
                                                                        #   to the list of ninjas in this dojo instance
        return dojo

    # //// UPDATE //////////////////////////////////////////////////////////

    # **** Update One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def update_one(cls, data:dict):
        query = "UPDATE " + TABLENAME +" SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        return connectToMySQL(TARGETDATABASE).query_db(query, data)

    # //// DELETE //////////////////////////////////////////////////////////

    # **** Delete One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def delete(cls, data:dict):
        query = "DELETE FROM " + TABLENAME + " WHERE id=%(id)s"
        return connectToMySQL(TARGETDATABASE).query_db(query, data)