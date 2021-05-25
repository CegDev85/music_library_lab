import pdb
from models.artist import Artist
import repositories.artist_repository as artist_repository



artist1 = Artist("Foo Fighters")
artist_repository.save(artist1)

artists_names = artist_repository.select_all()
# print(artists_names)

pdb.set_trace()