
from flask_app import app
from flask import render_template, redirect,request, session
from flask_app.models.models_dojos import Dojo
from flask_app.models.models_ninjas import Ninja






@app.route('/ninjas')
def show_add():
    dojos = Dojo.get_all()
    return render_template('show.html', dojos = dojos)

@app.route('/create', methods= ['POST'])
def create_ninja():
    dojo_data={
        # **request.form,
        # "id":id
        "dojo_id":request.form["dojos"],
        "first_name" : request.form["first_name"],
        "last_name" :request.form["last_name"],
        "age" : request.form["age"]
        
    }
    Ninja.create(dojo_data)
    return redirect('/dojos')