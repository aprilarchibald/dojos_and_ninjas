
from flask_app import app
from flask import render_template, redirect,request, session
# from flask_app.models import models_dojos, models_ninjas
from flask_app.models.models_dojos import Dojo



@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    # context ={
    #     "dojos": models_dojo.Dojo.get_all()
    # }
    # return render_template('index.html', **context)
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id":id
    }
    dojos=Dojo.get_by_id(data)
    return render_template('dojo.html', dojos = dojos)


@app.route("/create/dojo", methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect ('/dojos')
    