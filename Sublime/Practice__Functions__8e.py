#python3 Practice__Functions__8e.py

from pprint import pprint

print("\n") #pizza.py:

def make_pizza(size, *toppings):
	"""Print requested toppings."""
	print("Preparing a " + str(size) 
						+ "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping.title())
	

make_pizza(16, 'pepperoni')
print("\n")
make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')


print("\n") #user_profile.py:

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about the user."""
	profile = {} #Holds the usee's profile.
	profile['first_name'] = first #Set Argument.
	profile['last_name'] = last #Set Argument.

	for key, value in user_info.items():
		profile[key] = value #For arbitrary values. ^

	return profile 

user_profile = build_profile('albert', 'einstein', location = 'princeton',
														field = 'physics')

pprint(user_profile)
print("\n")