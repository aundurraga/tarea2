from database import connect_database
from base64 import b64encode

def create_artist(name, age):
    flag_input = check_input(name, age)
    if flag_input:
        return "Input invalido", 400
    flag_existe, dict_artista = check_artist(name, False)
    if flag_existe:
        return dict_artista, 409
    

    db = connect_database()
    cursor = db.cursor()
    id_artist = b64encode(name.encode()).decode('utf-8')
    if len(id_artist) >= 22:
        id_artist = id_artist[:22]
    statement = "INSERT INTO artist(id, name, age, albums, tracks, self) VALUES (?, ?, ?, ?, ?, ?)"
    albums = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id_artist}/albums"
    tracks = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id_artist}/tracks"
    self_page = f"https://t2-tallerdeintegracion.herokuapp.com/artists/{id_artist}"
    cursor.execute(statement, [id_artist, name, age, albums, tracks, self_page])
    db.commit()
    return {"id": id_artist, "name": name, "age": age, "albums": albums, "tracks": tracks, "self": self_page}, 201