import flask
import sys
import os
from database import connect_database
import sqlite3 

connect_database()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Api tarea 2</h1>"



"Creamos los elementos de la base de datos: POST"


"""@app.route("/artists", methods=["POST"])"""


if __name__ == "__main__":
    app.run(debug=True)