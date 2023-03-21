from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository


def save(album):
    sql = "INSERT INTO albums(name, artist_id, year) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.artist.id, album.year]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]    
    results = run_sql(sql, values)

    if len(results) > 0:
        selected_album = results[0]
        artist = artist_repository.select(selected_album["artist_id"])
        album = Album(
            selected_album["name"],
            artist,
            selected_album["year"],
            selected_album["id"]
        )
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        #create new task object
        new_album = Album(row["name"], 
                          artist, 
                          row["year"], 
                          row["id"]
                          )
        # append to list
        albums.append(new_album)
    return albums





            









# def delete(album):

# def update(album):

# def albums_for_artists(artist):