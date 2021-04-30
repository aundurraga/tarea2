from database import connect_database
from base64 import b64encode
from check import check_album, check_artista, check_track, artist_new, album_new, track_new

def create_artist(name, age):
    if type(name) != str or type(age) != int:
        return "Input invalido", 400
    existe = artist_new(name)
    if existe !=0:
        return existe, 409

    db = connect_database()
    cursor = db.cursor()
    id = b64encode(name.encode()).decode('utf-8')
    if len(id)>22:
        id= id[0:22]
    albums = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id}/albums"
    tracks = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id}/tracks"
    self_artist= f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id}"
    cursor.execute("INSERT INTO artist(id, name, age, albums, tracks, self) VALUES (?, ?, ?, ?, ?, ?)", [id, name, age, albums, tracks, self_artist])
    db.commit()
    return [{"id": id, "name": name, "age": age, "albums": albums, "tracks": tracks, "self": self_artist}, 201]

def create_album(id_artista, name, genre):
    if type(name) != str or type(genre) != str:
        return "Input invalido", 400
    if len(id_artista)>22:
        id_artista = id_artista[0:22]
    existe = check_artista(id_artista)
    if existe ==0:
         return "No existe artista", 422
    existe_album = album_new(name)
    if existe_album !=0:
        return existe_album, 409
    db = connect_database()
    cursor = db.cursor()
    id = b64encode(name.encode()).decode('utf-8')
    if len(id) >= 22:
        id = id[:22]
    artista = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id_artista}"
    tracks = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id}/tracks"
    self_album= f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id}"
    cursor.execute("INSERT INTO album(id, artist_id, name, genre, artist, tracks, self) VALUES (?, ?, ?, ?, ?, ?, ?)", [id, id_artista, name, genre, artista, tracks, self_album])
    db.commit()
    return [{"id": id, "id_artist": id_artista, "name": name, "genre": genre, "artist": artista, "tracks": tracks, "self": self_album}, 201]

def create_track(id_album, name, duration):
    if type(name) != str or type(duration) != float:
        return "Input invalido", 400
    if len(id_album)>22:
        id_album = id_album[0:22]
    existe = check_album(id_album)
    if existe ==0:
         return "No existe album", 422
    existe_track= track_new(name)
    if existe_track!=0:
        return existe_track, 409
    db = connect_database()
    cursor = db.cursor() 
    id = b64encode(name.encode()).decode('utf-8')
    if len(id) >= 22:
        id = id[:22]
   
    id_artista = cursor.execute("SELECT artist_id FROM album WHERE id = ?", [id_album]).fetchone()
    artista = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id_artista[0]}"
    album = f"https://t2-tallerdeintegracion.herokuapp.com/albums/{id_album}"
    self_track= f"https://t2-tdi.herokuapp.com/tracks/{id_album}"
    cursor.execute("INSERT INTO track(id, album_id, name, duration, times_played, artist, album, self) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [id, id_album, name, duration, 0, artista, album, self_track])
    db.commit()
    return [{"id": id, "album_id": id_album, "name": name, "duration": duration, "times_played": 0, "artist": artista, "album": album, "self": self_track}, 201]
