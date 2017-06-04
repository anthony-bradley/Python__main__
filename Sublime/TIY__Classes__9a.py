#python3 TIY__Classes__9a.py

#Restaurant: 9-1:
class Restaurant():
	"""A restaurant class."""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Names the restaurant and cusine type."""
		print("The name of this restaurant is " + 
			self.restaurant_name.title() + ".")
		print("This restaturant serves " + self.cuisine_type.title() +
			" cuisine.")

	def open_restaurant(self):
			"""Indicates that the restaurant is open."""
			print(self.restaurant_name.title() + " is open!")


restaurant = Restaurant('sushinista', 'japanese')

restaurant.describe_restaurant()
restaurant.open_restaurant()


#Three Restaurants: 9-2:

restaurant_1 = Restaurant('top dog', 'american')
restaurant_2 = Restaurant('fatapples', 'french-american')
restaurant_3 = Restaurant('au coquelet', 'french-american')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


#User: 9-3:

class User():
	"""A User class."""

	def __init__(
		self, first_name,
		last_name, age, hometown, birthplace):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hometown = hometown
		self.birthplace = birthplace

	def describe_user(self):
		"""Prints a summary of the user's information."""

		#full_name = (self.first_name + self.middle_name + self.last_name)

		#print("Name: " + self.full_name.title())
		print("Name: " + (self.first_name + " " + self.last_name).title())
		print("Age: " + self.age)
		print("Hometown: " + self.hometown.title())
		print("Birtplace: " + self.birthplace.title())

	def greet_user(self):
		"""Greets user."""
		print("Hello " + self.first_name.title() + "," + " Welcome!")


user_1 = User('anthony', 'thudium', str(24), 'berkeley', 'berkeley')

user_1.describe_user()
user_1.greet_user()


user_2 = User('david', 'safi', str(22), 'berkeley', 'nashville')

user_2.describe_user()
user_2.greet_user()


user_3 = User('dan', 'king', str(24), 'berkeley', 'san diego')

user_3.describe_user()
user_3.greet_user()









