#python3 practice8a.py

def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()


def greet_user(username):
	"""Display a simple greeting."""
	print("Hello " + username.title() + "!")

greet_user('tony')
