# ////////////////////////////////////////////////////////
# DOJOS CONTROLLER
# ////////////////////////////////////////////////////////

from flask_app import app
from flask import render_template, session, redirect, request, flash
import flask_app
from flask_app.models import users_class

# //// SHOW /////////////////////////////////////

@app.route('/dojos/')
@app.route('/dojos')                                                         # Main Page
def dojos():
    print("******** in dojos main page *******************")
    return render_template("dojos.html")

@app.route('/')                                                         # Main Page
def index():
    return redirect("/dojos")

@app.route('/users/new')                                                # **** FORM **** Create 1 New Users Page
def users_new():
    print("******** in New Users *******************")
    return render_template("create.html")

@app.route('/users/<int:id>/update')                                      # **** FORM **** Edit 1 User Page
def users_id_updqte(id):
    print("********* In Users ID Edit ****************")
    data = {
        'id': id
    }
    user = users_class.Users.get_one(data)                                          # Retrieve an instance of the user with the given ID
    return render_template("users_id_update.html", user=user)

# //// CREATE ////////////////////////////////////

@app.route('/users/new/post', methods=['POST'])                         # Retrieve the input values from create form
def users_new_post():
    print("**** In Users New Post Retrieval **************")
    data = {                                                            # Create Data Dictionary from values in form
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print(data)
    users_class.Users.save(data)                                        # Insert data retrieved into users database
    return redirect("/users")

# //// RETRIEVE ////////////////////////////////////

@app.route('/users/')
@app.route('/users')                                                    # Read All Users Page
def users():
    print("**** Retrieving Users *******************")
    all_users = users_class.Users.get_all()                             # Get all instances of users from the database
    return render_template("read_all.html", all_users = all_users)

@app.route('/users/<int:id>')                                           # Retrive the data from one specified user
def users_id (id):
    print ("*********** In users id ******************")
    data = {
        'id': id
    }
    user = users_class.Users.get_one(data)
    return render_template("users_read_one.html", user=user)

# //// UPDATE ////////////////////////////////////

@app.route('/users/<int:id>/update/post', methods=['POST'])             # Update a specified user's information
def users_id_update_post(id):
    print ("*********** In Users ID Edit POST *****************")
    data = {                                                            # retrieve the data from the form
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    users_class.Users.update_one(data)
    return redirect('/users')

# //// DELETE ////////////////////////////////////

@app.route('/users/<int:id>/delete')                                    # Delete a specified user
def users_id_delete(id):
    print("******** IN DELETE ********************")
    data = {
        'id': id
    }
    users_class.Users.delete(data)
    return redirect('/users')

# //// 404 CATCH //////////////////////////////////

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."