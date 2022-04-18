from flask import Flask
app = Flask(__name__)
app.secret_key = "security"

DATABASE ="dojos_and_ninjas"

from flask_app.controllers import controller_ninjas, controller_dojos

