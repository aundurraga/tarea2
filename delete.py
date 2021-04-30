from database import connect_database
from base64 import b64encode
from check import check_album, check_artista, check_track, artist_new, album_new, track_new




def delete_track_id(id):
    existe = check_track(id)
    if existe ==0:
        return ["No existe el track", 404]
    else:
        db = connect_database()
        cursor = db.cursor()
        tracks = cursor.execute("DELETE FROM track WHERE id = ?", [id]).fetchall()
        db.commit()
    return ["Track eliminado", 204]

def delete_album_id(id):
    existe = check_album(id)
    if existe ==0:
        return ["No existe el album", 404]
    else:
        db = connect_database()
        cursor = db.cursor()
        tracks = cursor.execute("DELETE FROM album WHERE id = ?", [id]).fetchall()
        db.commit()
    return ["Album eliminado", 204]

def delete_artist_id(id):
    existe = check_artista(id)
    if existe ==0:
        return ["No existe el artista", 404]
    else:
        db = connect_database()
        cursor = db.cursor()
        tracks = cursor.execute("DELETE FROM artist WHERE id = ?", [id]).fetchall()
        db.commit()
    return ["Artista eliminado", 204]