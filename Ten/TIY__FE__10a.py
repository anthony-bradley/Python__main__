#python3 TIY__FE__10a.py

import json

#Favorite Number: 10-11:

filename = 'favorite_number.json'

try:
	with open(filename) as file_object:
		favorite_number = json.load(file_object)

except FileNotFoundError:
	favorite_number = input("What is your favorite number? ")
	with open(filename, 'w') as file_object:
		json.dump(favorite_number, file_object)
		print("Your favorite number is stored!")
else:
	print("I know your favorite number! It's " + favorite_number + "." )


#Favorite Number Remembered: 10-12:

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("Name: ")
	filename = 'username.json'
	with open(filename, 'w') as file_object:
		json.dump(username.title(), file_object)
		return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		correct = input("Are you " + username + "? (y/n) ")
		if correct == 'y':
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
			print(username.title())

greet_user()