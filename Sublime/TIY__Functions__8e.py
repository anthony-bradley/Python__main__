#python3 TIY__Functions__8e.py

from pprint import pprint

print("\n") #Sandwiches: 8-12:

def make_sandwich(*fillings):
	"""Makes a sandwich with an arbitrary number of fillings."""
	print("Preparing a sandwich with the following fillings: ")

	for filling in fillings:
		print("- " + filling.title())

	print("\n")

make_sandwich('turkey', 'avodcado')
make_sandwich('pastrami')
make_sandwich('bacon', 'lettuce', 'tomato')


print("\n") #User Profile: 8-13:

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about the user."""
	profile = {} #Holds the usee's profile.
	profile['first_name'] = first #Set Argument.
	profile['last_name'] = last #Set Argument.

	for key, value in user_info.items():
		profile[key] = value #For arbitrary values. ^

	return profile 

user_profile = build_profile('anthony', 'thudium', location = 'berkeley',
													occupation = 'CEO')

pprint(user_profile)


print("\n") #Cars: 8-14:

def make_car(manufacturer, model, **other_info):
	"""Store information about a specific car in a dictionary."""
	details = {}
	details['manufacturer'] = manufacturer
	details['model'] = model

	for key, value in other_info.items():
		details[key] = value

	return details

car = make_car('tesla', 'model s', doors = 4, color = 'cardinal')

print(car)
print("\n")