"""cd desktop/python/sublime
   python3 tiy6c.py
"""

print("\n")	#6-7:

best_friends = {
	'glen':{
		'first': 'glen',
		'last': 'engle',
		'age': 24,
		'location': 'el cerrito',
		'hair_color': 'blonde',
		'eye_color' : 'anachronistic',	#['anachronistic', 'blue', 'green'],
	},
	'mike':{
		'first': 'michael',
		'last': 'jovez',
		'age': 24,
		'location': 'pinole',
		'hair_color': 'black',
		'eye_color': 'dark brown',
	},
	'david':{
		'first': 'david',
		'last': 'safi',
		'age': 22,
		'location': 'berkeley',
		'hair_color': 'black',
		'eye_color': 'dark brown',
	},
}

for friends_names, friends_info in best_friends.items():

	#print("Name: " + friends_names)

	full_name = friends_info['first'] + " " + friends_info['last']
	age = friends_info['age']
	location = friends_info['location']
	hair_color = friends_info['hair_color']
	eye_color = friends_info['eye_color']
	
	print("Name: " + friends_names.title())
	print("\t Full name: " + full_name.title())
	print("\t Age: " + str(age))
	print("\t Location: " + location.title())
	print("\t Hair Color: " + hair_color.title())
	print("\t Eye Color: " + eye_color.title())
	print("\n")
	#for eye_colors in eye_color:
		#print("Eye Color: " + eye_colors.title())

print("\n")	#6-8. Pets: 

pets = {
	'thor':{
		'breed': 'doberman',
		'owner': 'scott thudium',
	},
	'sheeba':{
		'breed': 'siberian husky',
		'owner': 'ivan cruz',
	},
}

for pet_name, pet_info in pets.items():
	print("Name of Dog: " + pet_name.title())
	print("\tBreed: " + pet_info['breed'].title())
	print("\tOwner: " + pet_info['owner'].title())
	print("\n")

print("\n")	#6-9. Favorite Places:

"""
favorite_places = {
	'mike':{
		'locations':{
			'pinole',
			'san francisco',
		},
	},
	'glen':{
		'locations': ['el cerrito', 'fremont', 'santa barbara'],
	},
	'matt':{
		'locations': ['santa cruz', 'el sobrante'],
	},
}
"""

favorite_places = {
	'mike':{
		'locations': ['pinole', 'san francisco'],
	},
	'glen':{
		'locations': ['el cerrito', 'fremont', 'santa barbara'],
	},
	'matt':{
		'locations': ['santa cruz', 'el sobrante'],
	},
}

for person, persons_info in favorite_places.items():
	print("Name: " + person.title())
	print("\t\nFavorite destinations: " + str(persons_info['locations']))
	print("\n\n")

print("\n")	#6-10. Favorite Numbers:

favorite_numbers = {
	'glen': [11, 12, 13, 14],
	'mike': [23, 24, 25],
	'tony': [7, 8, 9, 10],
	'alyse': [12, 13, 14, 15],
}

for person, numbers in favorite_numbers.items():
	print("Name: " + person.title())
	print("\t\n Favorite Numbers: " + str(numbers))
	print("\n")

print("\n")	#6-11. Cities:

cities = {
	'new york city':{
		'state': 'new york',
		'country': 'united states',
		'population': 8500000,
		'fact': 'nyc is comprised of 5 boroughs.',
	},
	'chicago':{
		'state': 'illinois',
		'country': 'united states',
		'population': 2750000,
		'fact':'home to lake michigan.',
	},
	'munich':{
		'state': 'bavaria',
		'country': 'germany',
		'population': 1500000,
		'fact': '12th biggest city of the european union.',
	},
}



for city, info in cities.items():
	population_string = info['population']
	print("Name of City: " + city.title())
	print("\tState: " + info['state'].title())
	print("\tCountry: " + info['country'].title())
	print("\tPopulation: " + str(population_string))
	print("\tFun Fact: " + info['fact'].title())
	print("\n")

print("\n")	#6-12. Extensions:



















































	