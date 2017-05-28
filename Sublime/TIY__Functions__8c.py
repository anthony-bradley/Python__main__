#python3 TIY__Functions__8c.py


print("\n") #City Names: 8-6:

def city_country(city, country):
	"""Returns the name of a city and its corresponding country."""
	return(city.title() + ', ' + country.title())

location_1 = city_country('santiago', 'chile')
print (location_1)

location_2 = city_country('lima', 'peru')
print (location_2)

location_3 = city_country('chicago', 'united states')
print (location_3)


print("\n") #Album: 8-7:

def make_album(artist, album, tracks = ''):
	"""Builds a dictionary describing a music album."""
	album = {
		'artist'.title(): artist.title(), 
		'album'.title(): album.title(),
		}
	if tracks:
		album['tracks'.title()] = tracks
	#return(album['artist'] + ', ' + album['album'])
	return album

album_1 = make_album('michael jackson', 'thriller')
print(album_1)

album_2 = make_album('begees', 'saturday night fever')
print(album_2)

album_3 = make_album('eagles', 'hotel california', tracks = 9)
print(album_3)


print("\n") #User Albums: 8-8:

def make_album(artist, album, tracks = ''):
	"""Builds a dictionary describing a music album."""
	album = {
		'artist'.title(): artist.title(), 
		'album'.title(): album.title(),
		}
	if tracks:
		album['tracks'.title()] = tracks
	#return(album['artist'] + ', ' + album['album'])
	return album

while True:
	print("\n~ Please enter your own albums ~")
	print("(Press 'q' at any time to exit the program.)")

	artist_name = input("\nArtist Name: ")
	if artist_name == 'q':
		break

	album_name = input("\nAlbum Name: ")
	if album_name == 'q':
		break

	user_album = make_album(artist_name, album_name)
	print("\n\nVery Nice! You've chosen: ")
	print(user_album)