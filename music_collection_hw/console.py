from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


# artist_1 = Artist("The Black Keys")
# artist_repository.save(artist_1)

# artist_2 = Artist("Bombay Bicycle Club")
# artist_repository.save(artist_2)

# album_1 = Album("I Had the Blues But I Shook Them Loose", artist_2, 2008)
# album_repository.save(album_1)
# album_2 = Album("A Different Kind of Fix", artist_2, 2011)
# album_repository.save(album_2)
# album_3 = Album("So Long, See You Tomorrow", artist_2 , 2014)
# album_repository.save(album_3)
# album_4 = Album("Everything Else Has Gone Wrong", artist_2 , 2019)
# album_repository.save(album_4)
# album_5 = Album("Brothers", artist_1, 2010)
# album_repository.save(album_5)
# album_6 = Album("El Camino", artist_1, 2011)
# album_repository.save(album_6)
# album_7 = Album("Turn Blue", artist_1, 2014)
# album_repository.save(album_7)
# album_8 = Album("Lets Rock", artist_1, 2019)
# album_repository.save(album_8)
# album_9 = Album("Delta Kream", artist_1, 2021)
# album_repository.save(album_9)
# album_9 = Album("Dropout Boogie", artist_1, 2022)

# album_repository.delete_all()
# artist_repository.delete_all()

# result = album_repository.select_all()

# for album in result:
#     print(album.name)

result = artist_repository.select_all()

for artist in result:
    print(artist.name)

# result = album_repository.select(62)

# print(result.name)

# result = artist_repository.select(16)

# print(result.name)