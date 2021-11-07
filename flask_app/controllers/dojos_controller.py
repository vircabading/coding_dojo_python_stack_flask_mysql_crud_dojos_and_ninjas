# ////////////////////////////////////////////////////////
# DOJOS CONTROLLER
# ////////////////////////////////////////////////////////

from flask_app import app
from flask import render_template, session, redirect, request, flash
import flask_app
from flask_app.models import dojos_model, ninjas_model

# //// SHOW /////////////////////////////////////

@app.route('/')                                                     # Main Page
def index():
    return redirect("/dojos")                                       # Redirects to get all the dojos page


# //// CREATE ////////////////////////////////////

# **** Create a New Dojo *************************
@app.route('/dojos/post', methods=['POST'])                             # Retrieve the input values from create form
def dojos_post():
    print("**** In Dojos Post **************")
    data = {                                                            # Create Data Dictionary from values in form
        'name': request.form['name'],
    }
    print("Data is:")
    print(data)
    dojos_model.Dojos.dojos_create(data)                                # Create a New Dojo
    return redirect("/dojos")

# **** Create a New Ninja *************************
@app.route('/ninjas/create/post', methods=['POST'])                     # Retrieve the input values from create form
def ninjas_create_post():
    print("**** In Ninjas Create Post **************")
    data = {                                                            # Create Data Dictionary from values in form
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    print("Data is:")
    print(data)
    print("Ninja id of ninja created:")
    result = ninjas_model.Ninjas.create(data)                           # Create a new ninja on the database
    return redirect(f"/dojos/{ data['dojo_id'] }")

# //// RETRIEVE ////////////////////////////////////

# **** GET ALL DOJOS *******************************
@app.route('/dojos/')
@app.route('/dojos')                                                    # Read All Page
def dojos():
    print("**** Retrieving Dojos *******************")
    all_dojos = dojos_model.Dojos.get_all()                             # Get all instances of from the database
    return render_template("dojos_show.html", all_dojos = all_dojos)

# **** GET ALL THE DOJOS SO WE CAN CREATE A NEW NINJA
@app.route("/ninjas/create")
def ninjas_create():
    all_dojos = dojos_model.Dojos.get_all()                             # Get all instances of from the database
    return render_template("ninjas_create.html", all_dojos = all_dojos)

# **** GET DOJO WITH ALL ITS NINJAS ****************
@app.route('/dojos/<int:id>')                                          
def dojos_id(id):
    print("**** Retrieving Dojo with all its Ninjas ********")
    data = {
        'id': id
    }
    print("Data ************")
    print(data)
    dojo = dojos_model.Dojos.get_dojo_with_ninjas(data)
    return render_template("dojo_ninjas_show.html", dojo = dojo)

# //// UPDATE ////////////////////////////////////


# //// DELETE ////////////////////////////////////


# //// 404 CATCH //////////////////////////////////

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."