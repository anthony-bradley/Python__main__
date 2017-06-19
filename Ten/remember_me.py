#python3 remember_me.py

import json

#username = input("Name: ")

#filename = 'username.json'
#with open(filename, 'w') as file_object:
#	json.dump(username.title(), file_object)
#	print(username.title() 
#		+ ", your information has been stored for later use.")


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
		json.dump(username, file_object)
		return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print(username.title() 
			+ ", your information has been stored for later use.")


#def greet_user():
#	"""Greet the user by name."""
#
#	filename = 'username.json'

#	try:
#		with open(filename) as file_object:
#			username = json.load(file_object)
#	except FileNotFoundError:
#		username = input("Name: ")
#		with open(filename, 'w') as file_object:
#			json.dump(username.title(), file_object)
#			print(username.title() 
				#+ ", your information has been stored for later use.")
#	else:
#		print("Welcome back, " + username + "!")


greet_user()