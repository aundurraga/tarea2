from database import connect_database
from base64 import b64encode


def check_artista(id):
    db = connect_database()
    cursor = db.cursor()
    artista = cursor.execute("SELECT id, name, age, albums, tracks, self FROM artist WHERE id=?", [id]).fetchone()
    if artista:
        return {"id": artista[0], "name": artista[1], "age": artista[2], "albums": artista[3], "tracks": artista[4], "self": artista[5]}
    else:
        return 0

def check_album(id):
    db = connect_database()
    cursor = db.cursor()
    album = cursor.execute("SELECT id, artist_id, name, genre, artist, tracks, self FROM album WHERE id=?", [id]).fetchone()
    print(id)
    if album:
        return {"id": album[0], "artist_id": album[1], "name": album[2], "genre": album[3],"artist": album[4], "tracks": album[5], "self": album[6]}
    else:
        return 0

def check_track(id):
    db = connect_database()
    cursor = db.cursor()
    track = cursor.execute("SELECT id, album_id, name, duration, times_played, artist, album, self FROM track WHERE id=?", [id]).fetchone()
    if track:
        return {"id": track[0], "album_id": track[1], "name": track[2], "duration": track[3], "times_played": track[4],"artist": track[5],"album": track[6], "self": track[7]}
    else:
        return 0

def artist_new(name):
    id = b64encode(name.encode()).decode('utf-8')
    if len(id) >= 22:
        id = id[:22]
    db = connect_database()
    cursor = db.cursor()
    artista = cursor.execute("SELECT  id, name, age, albums, tracks, self FROM artist WHERE id=?", [id]).fetchone()
    if artista:
        return {"id": artista[0], "name": artista[1], "age": artista[2], "albums": artista[3], "tracks": artista[4], "self": artista[5]}
    else:
        return 0

def album_new(name,id_artista):
    name_id = f"{name}:{id_artista}"
    id = b64encode(name_id.encode()).decode('utf-8')
    if len(id) >= 22:
        id = id[0:22]
    
    db = connect_database()
    cursor = db.cursor()
    album = cursor.execute("SELECT id, artist_id, name, genre, artist, tracks, self FROM album WHERE id=?", [id]).fetchone()
    if album:
        return {"id": album[0], "artist_id": album[1], "name": album[2], "genre": album[3],"artist": album[4], "tracks": album[5], "self": album[6]}
    else:
        return 0

def track_new(name,id_album):
    name_track = f"{name}:{id_album}"
    id= b64encode(name_track.encode()).decode('utf-8')
    if len(id) >= 22:
        id = id[0:22]
    
    db = connect_database()
    cursor = db.cursor()
    track = cursor.execute("SELECT id, album_id, name, duration, times_played, artist, album, self FROM track WHERE id = ?", [id]).fetchone()
    if track:
        return {"id": track[0], "album_id": track[1], "name": track[2], "duration": track[3], "times_played": track[4],"artist": track[5],"album": track[6], "self": track[7]}
    else:
        return 0
