import sqlite3


table_artists = """CREATE TABLE IF NOT EXISTS artist(id TEXT PRIMARY KEY,name TEXT,
				age INTEGER, albums TEXT, tracks TEXT, self TEXT)"""
table_albums = """CREATE TABLE IF NOT EXISTS album(id TEXT PRIMARY KEY, artist_id TEXT,
				name TEXT, genre TEXT,artist TEXT,tracks TEXT,
                self TEXT,FOREIGN KEY(artist_id) REFERENCES artist(id) ON DELETE CASCADE)"""
table_tracks = """CREATE TABLE IF NOT EXISTS track(id TEXT PRIMARY KEY, album_id TEXT,name TEXT,duration FLOAT,
                times_played INTEGER,artist TEXT,album TEXT,self TEXT,FOREIGN KEY(album_id) REFERENCES album(id) ON DELETE CASCADE)"""


def connect_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.execute(table_artists)
    cursor.execute(table_albums)
    cursor.execute(table_tracks)
    conn.commit()
    return conn




