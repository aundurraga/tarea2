from database import connect_database
from base64 import b64encode
from check import check_album, check_artista, check_track, artist_new, album_new, track_new

def put_artist_tracks(id):
    existe = check_artista(id)
    if existe ==0:
        return "No existe el artista", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        albums = cursor.execute("SELECT id FROM album WHERE artist_id=?", [id]).fetchall()
        lista = []
        for album in albums:
            id_album = album[0]
            times = cursor.execute("SELECT times_played FROM track WHERE album_id=?", [id_album]).fetchone()
            print(id_album)
            cursor.execute("UPDATE track SET times_played = ? WHERE album_id = ?", [int(times[0])+1, id_album])
            db.commit()
        return ["Played", 200] 

def put_album_tracks(id):
    existe = check_album(id)
    if existe ==0:
        return "No existe el album", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        tracks = cursor.execute("SELECT times_played FROM track WHERE album_id=?", [id]).fetchall()
        for track in tracks:
            times = track[0]
            cursor.execute("UPDATE track SET times_played = ? WHERE album_id = ?", [int(times)+1, id])
            db.commit()
        return ["Played", 200] 

def put_tracks(id):
    existe = check_track(id)
    if existe ==0:
        return "No existe el track", 404
    else:
        db = connect_database()
        cursor = db.cursor()
        track = cursor.execute("SELECT times_played FROM track WHERE id=?", [id]).fetchall()
        times = track[0]
        cursor.execute("UPDATE track SET times_played = ? WHERE id = ?", [int(times[0])+1, id])
        db.commit()
        return ["Played", 200] 