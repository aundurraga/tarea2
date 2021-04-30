from database import connect_database
from base64 import b64encode
from check import check_album, check_artista, check_track



def get_artist():
    db = connect_database()
    cursor = db.cursor()
    lista = []
    artistas = cursor.execute("SELECT id, name, age, albums, tracks, self FROM artist").fetchall()
    for artist in artistas:
        lista.append({"id": artist[0], "name": artist[1], "age": artist[2], "albums": artist[3], "tracks": artist[4], "self": artist[5]})
    return [lista, 200] 

def get_album():
    db = connect_database()
    cursor = db.cursor()
    albums = cursor.execute("SELECT id, artist_id, name, genre, artist, tracks, self FROM album").fetchall()
    lista = []
    for album in albums:
        lista.append({"id": album[0], "artist_id": album[1], "name": album[2], "genre": album[3],"artist": album[4], "tracks": album[5], "self": album[6]})
    return [lista, 200] 

def get_track():
    db = connect_database()
    cursor = db.cursor()
    tracks = cursor.execute("SELECT id, album_id, name, duration, times_played, artist, album, self FROM track").fetchall()
    lista = []
    for track in tracks:
        lista.append({"id": track[0], "album_id": track[1], "name": track[2], "duration": track[3], "times_played": track[4],"artist": track[5],"album": track[6], "self": track[7]})
    return [lista, 200] 

def get_artist_id(id):
    existe = check_artista(id)
    if existe ==0:
        return "No existe el artista", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        artista = cursor.execute("SELECT id, name, age, albums, tracks, self FROM artist WHERE id=?",[id]).fetchone()
        lista = [{"id": artista[0], "name": artista[1], "age": artista[2], "albums": artista[3], "tracks": artista[4], "self": artista[5]}]
        return [lista, 200] 

def get_artist_id_albums(id):
    existe = check_artista(id)
    if existe ==0:
        return "No existe el artista", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        albums = cursor.execute("SELECT id, artist_id, name, genre, artist, tracks, self FROM album WHERE artist_id=?", [id]).fetchall()
        lista = []
        for album in albums:
            lista.append({"id": album[0], "artist_id": album[1], "name": album[2], "genre": album[3],"artist": album[4], "tracks": album[5], "self": album[6]})
        return [lista, 200] 

def get_artist_id_tracks(id):
    existe = check_artista(id)
    if existe ==0:
        return "No existe el artista", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        albums = cursor.execute("SELECT id, artist_id, name, genre, artist, tracks, self FROM album WHERE artist_id=?", [id]).fetchall()
        lista = []
        for album in albums:
            tracks = cursor.execute("SELECT id, album_id, name, duration, times_played, artist, album, self FROM track WHERE album_id=?", [album[0]]).fetchall()
            for track in tracks:
                lista.append({"id": track[0], "album_id": track[1], "name": track[2], "duration": track[3], "times_played": track[4],"artist": track[5],"album": track[6], "self": track[7]})
        return [lista, 200] 

def get_album_id(id):
    existe = check_album(id)
    if existe ==0:
        return "No existe el album", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        album = cursor.execute("SELECT id, artist_id, name, genre, artist, tracks, self FROM album WHERE id=?", [id]).fetchone()
        lista = [{"id": album[0], "artist_id": album[1], "name": album[2], "genre": album[3],"artist": album[4], "tracks": album[5], "self": album[6]}]
        return [lista, 200] 

def get_album_id_tracks(id):
    existe = check_album(id)
    if existe ==0:
        return "No existe el album", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        lista = []
        tracks = cursor.execute("SELECT id, album_id, name, duration, times_played, artist, album, self FROM track WHERE album_id=?", [id]).fetchall()
        for track in tracks:
            lista.append({"id": track[0], "album_id": track[1], "name": track[2], "duration": track[3], "times_played": track[4],"artist": track[5],"album": track[6], "self": track[7]})
        return [lista, 200] 

def get_track_id(id):
    existe = check_track(id)
    if existe ==0:
        return "No existe la cancion", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        track = cursor.execute("SELECT id, album_id, name, duration, times_played, artist, album, self FROM track WHERE id=?", [id]).fetchone()
        lista = [{"id": track[0], "album_id": track[1], "name": track[2], "duration": track[3], "times_played": track[4],"artist": track[5],"album": track[6], "self": track[7]}]
        return [lista, 200] 
