#python3 TIY__Functions__8b.py

print("\n") #8-3:

def make_shirt(size, text):
	"""T-Shirt."""
	print("Your t-shirt is a size " + size.title() + ".")
	print("Your t-shirt will read the message \"" + text + "\"")

make_shirt('medium', 'CS rocks!') #Positional.
make_shirt(size = 'large', text = 'Sup.') #Keyword.


print("\n") #8-4:

def make_shirt(size = 'large', text = 'I love Python.'):
	"""Large Shirts."""
	print("Your t-shirt is a size " + size.title() + ".")
	print("Your t-shirt will read the message \"" + text + "\"")

make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', text = "I'm with stupid.")


print("\n") #8-5:

def describe_city(city, country = 'united states'):
	"""Cities."""
	print(city.title() + " is in the " + country.title() + ".")

describe_city('chicago')
describe_city('san francisco')