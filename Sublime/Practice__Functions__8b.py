#python3 Practice8b.py

#pets.py:

def describe_pet(animal_type, pet_name): 
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'thor')
describe_pet('whale', 'willy')


def describe_pet(animal_type, pet_name): 
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('thor', 'dog')
describe_pet('willy', 'whale')


def describe_pet(animal_type, pet_name): 
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'dog', pet_name = 'thor')
describe_pet(pet_name = 'thor', animal_type = 'dog')


def describe_pet(pet_name, animal_type = 'dog'): 
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('thor')
