import flask
import sys
import os
from database import connect_database
import get,post, put,delete
import sqlite3 

connect_database()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Api tarea 2</h1>"


@app.route('/artists', methods=["GET", "POST", "DELETE", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW" ])
def artist():
    if flask.request.method == "GET":
        resultado = get.get_artist()
        return flask.jsonify(resultado[0]), resultado[1]

    elif flask.request.method == "POST":
        info = flask.request.get_json()
        if type(info) == type(None) or info == {}:
            name = None
            age = None
        else:
            if("name" in info): 
                name = info["name"]
            else:
                name = None
            if("age" in info): 
                age = info["age"]
            else:
                age = None
        resultado = post.create_artist(name, age)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return jsonify("Este metodo no está permitido"), 405

@app.route('/albums', methods=["GET", "POST", "DELETE", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW" ])
def get_album():
    if flask.request.method == "GET":
        resultado = get.get_album()
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/tracks', methods=["GET","POST", "DELETE", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"])
def get_track():
    if flask.request.method == "GET":
        resultado = get.get_track()
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405


@app.route('/artists/<id>', methods=["GET","DELETE","POST", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"  ])
def artist_id(id):
    if flask.request.method == "GET":
        resultado = get.get_artist_id(id)
        return flask.jsonify(resultado[0]), resultado[1]

    elif flask.request.method == "DELETE":
        resultado = delete.delete_artist_id(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/artists/<id>/albums', methods=["GET","POST","DELETE", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"  ])
def artist_id_albums(id):
    if flask.request.method == "GET":
        resultado = get.get_artist_id_albums(id)
        return flask.jsonify(resultado[0]), resultado[1]
    elif flask.request.method == "POST":
        info = flask.request.get_json()
        if type(info) == type(None) or info == {}:
            name = None
            genre = None
        else:
            if("name" in info): 
                name = info["name"]
            else:
                name = None
            if("genre" in info): 
                genre = info["genre"]
            else:
                genre = None
        resultado = post.create_album(id, name, genre)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/artists/<id>/tracks', methods=["GET","POST", "DELETE", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"])
def get_artist_id_tracks(id):
    if flask.request.method == "GET":
        resultado = get.get_artist_id_tracks(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/albums/<id>', methods=["GET", "DELETE","POST", "PUT","PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW" ])
def album_id(id):
    if flask.request.method == "GET":
        resultado = get.get_album_id(id)
        return flask.jsonify(resultado[0]), resultado[1]

    elif flask.request.method == "DELETE":
        resultado = delete.delete_album_id(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/albums/<id>/tracks', methods=["GET", "POST","DELETE", "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW" ])
def album_id_tracks(id):
    if flask.request.method == "GET":
        resultado = get.get_album_id_tracks(id)
        return flask.jsonify(resultado[0]), resultado[1]
    elif flask.request.method == "POST":
        info = flask.request.get_json()
        if type(info) == type(None) or info == {}:
            name = None
            duratiom = None
        else:
            if("name" in info): 
                name = info["name"]
            else:
                name = None
            if("duration" in info): 
                duration = info["duration"]
            else:
                duration = None
        resultado = post.create_track(id, name, duration)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/tracks/<id>', methods=["GET", "DELETE","POST",  "PUT", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"])
def track_id(id):
    if flask.request.method == "GET":
        resultado = get.get_track_id(id)
        return flask.jsonify(resultado[0]), resultado[1]
    elif flask.request.method == "DELETE":
        resultado = delete.delete_track_id(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return jsonify("Este metodo no está permitido"), 405





@app.route('/artists/<id>/albums/play', methods=["PUT","GET", "POST", "DELETE", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"])
def put_artist_tracks(id):
    if flask.request.method == "PUT":
        resultado = put.put_artist_tracks(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/albums/<id>/tracks/play', methods=["PUT","GET", "POST", "DELETE", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"])
def put_album_tracks(id):
    if flask.request.method == "PUT":
        resultado = put.put_album_tracks(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

@app.route('/tracks/<id>/play', methods=["PUT","GET", "POST", "DELETE", "PATCH", "COPY", "HEAD", "OPTIONS", "LINK", "UNLINK", "PURGE", "LOCK", "UNLOCK", "PROPFIND", "VIEW"])
def put_tracks(id):
    if flask.request.method == "PUT":
        resultado = put.put_tracks(id)
        return flask.jsonify(resultado[0]), resultado[1]
    else:
        return flask.jsonify("Este metodo no está permitido"), 405

if __name__ == "__main__":
    app.run(debug=True)