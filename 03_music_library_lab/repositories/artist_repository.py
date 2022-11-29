from db.run_sql import run_sql
from models.artist import Artist
import repositories.album_repository as banananas
from models.album import Album

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        artist = Artist(result['name'], result['id'])

    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'])
        artists.append(artist)
    return artists

def delete_all():
    sql = 'DELETE FROM artists'
    run_sql(sql)

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def all_albums(artist):
    albums = []
    sql = 'SELECT * FROM albums WHERE artist_id = %s'
    values = [artist.id]
    results = run_sql(sql, values)
    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums


def update(artist):
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"


