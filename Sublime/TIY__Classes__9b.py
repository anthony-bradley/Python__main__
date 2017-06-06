#python3 TIY__Classes__9b.py

#Number Served: 9-4: (Uses program from 9-1)

class Restaurant():
	"""A restaurant class."""

	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Names the restaurant and cusine type."""
		print("Restaurant Name: " + self.name.title())
		print("Cuisine Type: " + self.cuisine_type.title())

	def open_restaurant(self):
		"""Indicates that the restaurant is open."""
		print(self.name.title() + " is open!")

	def set_number_served(self, number_served):
		"""Number of customes served."""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Amount of customers served throughout the day."""
		self.number_served += additional_served


restaurant = Restaurant('sushinista', 'japanese') #Instance.
restaurant.describe_restaurant()


print("Number Served: " + str(restaurant.number_served))


restaurant.number_served = 200
print("Number Served: " + str(restaurant.number_served))


restaurant.set_number_served(1200)
print("Number Served: " + str(restaurant.number_served))

restaurant.increment_number_served(1400)
print("Number Served: " + str(restaurant.number_served))


#Login Attempts: 9-5:

class User():
	"""A User class."""

	def __init__(self, first_name, last_name, age, hometown, birthplace):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hometown = hometown
		self.birthplace = birthplace
		self.login_attempts = 0

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

	def increment_login_attempts(self):
		"""Increments the amount of login attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets value of login_attempts to 0."""
		self.login_attempts = 0


user_1 = User('anthony', 'thudium', str(24), 'berkeley', 'berkeley')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print("Login Attempts: " + str(user_1.login_attempts))


user_1.reset_login_attempts()
print("Login Attempts: " + str(user_1.login_attempts))