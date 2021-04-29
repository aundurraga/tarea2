import flask
import sys
import os
from database import connect_database
import artist, album, track
import sqlite3 

connect_database()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Api tarea 2</h1>"



"Creamos los elementos de la base de datos: POST"


@app.route("/artists", methods=["POST"])
def create_artist():
    artist_details = request.get_json()
    if type(artist_details) == type(None) or artist_details == {}:
        name = None
        age = None
    else:
        try: 
            name = artist_details["name"]
        except:
            name = None
        try: 
            age = artist_details["age"]
        except:
            age = None
    print(request.args.get("name"))
    print(age)
    result, codigo = artist.insert_artist(name, age)
    return jsonify(result), codigo


if __name__ == "__main__":
    app.run(debug=True)