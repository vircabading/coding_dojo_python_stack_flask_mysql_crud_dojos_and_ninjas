# ////////////////////////////////////////////////////////
# DOJOS CONTROLLER
# ////////////////////////////////////////////////////////

from flask_app import app
from flask import render_template, session, redirect, request, flash
import flask_app
from flask_app.models import dojos_model

# //// SHOW /////////////////////////////////////

@app.route('/')                                                     # Main Page
def index():
    return redirect("/dojos")                                       # Redirects to get all the dojos page

# //// CREATE ////////////////////////////////////

@app.route('/dojos/post', methods=['POST'])                             # Retrieve the input values from create form
def dojos_post():
    print("**** In Dojos Post **************")
    data = {                                                            # Create Data Dictionary from values in form
        'name': request.form['name'],
    }
    print("Date is:")
    print(data)
    dojos_model.Dojos.save(data)
    return redirect("/dojos")

# //// RETRIEVE ////////////////////////////////////

# **** GET ALL *************************************
@app.route('/dojos/')
@app.route('/dojos')                                                    # Read All Page
def dojos():
    print("**** Retrieving Dojos *******************")
    all_dojos = dojos_model.Dojos.get_all()                             # Get all instances of from the database
    return render_template("dojos.html", all_dojos = all_dojos)

# @app.route('/users/<int:id>')                                           # Retrive the data from one specified user
# def users_id (id):
#     print ("*********** In users id ******************")
#     data = {
#         'id': id
#     }
#     user = users_class.Users.get_one(data)
#     return render_template("users_read_one.html", user=user)

# //// UPDATE ////////////////////////////////////

# @app.route('/users/<int:id>/update/post', methods=['POST'])             # Update a specified user's information
# def users_id_update_post(id):
#     print ("*********** In Users ID Edit POST *****************")
#     data = {                                                            # retrieve the data from the form
#         'id': id,
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email': request.form['email']
#     }
#     users_class.Users.update_one(data)
#     return redirect('/users')

# //// DELETE ////////////////////////////////////

@app.route('/users/<int:id>/delete')                                    # Delete a specified user
def users_id_delete(id):
    print("******** IN DELETE ********************")
    data = {
        'id': id
    }
    dojos_model.Dojos.delete(data)
    return redirect('/users')

# //// 404 CATCH //////////////////////////////////

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."