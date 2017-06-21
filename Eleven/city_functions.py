#python3 city_functions.py

def city_country(city, country, population=''):
	"""Prints a city and its corresponding country."""
	if population:
		city_data = city + ", " + country + " - Population: " + str(population)
	else:
		city_data = city + ", " + country

	return city_data.title()

#print(city_country('santiago', 'chile'))
#print(city_country('santiago', 'chile', 500000))