import pdb
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Boards of Canada")
artist_repository.save(artist_1)

artist_2 = Artist("Eminem")
artist_repository.save(artist_2)

album_1 = Album("Tomorrows Harvest", "Electronica/Ambient", artist_1)
album_repository.save(album_1)
album_2 = Album("Real Slim Shady", "Hip-Hop", artist_2)
album_repository.save(album_2)
album_3 = Album("Music as the right to children", "Electronica/Ambient", artist_1)
album_repository.save(album_3)

found = artist_repository.select_all()
found_one = artist_repository.select(artist_1.id)

found_album = album_repository.select(album_1.id)
all_albums_BOC = artist_repository.all_albums(artist_1)

pdb.set_trace()

