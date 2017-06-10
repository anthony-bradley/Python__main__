#python3 TIY__Classes__9c.py

#Ice Cream Stand: 9-6:

class Restaurant():
	"""A restaurant class."""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Names the restaurant and cusine type."""
		print("\nRestaurant Name: " + self.restaurant_name.title())
		print("Cuisine Type: " + self.cuisine_type.title())

	def open_restaurant(self):
			"""Indicates that the restaurant is open."""
			print(self.restaurant_name.title() + " is open!")


class IceScreamStand(Restaurant):
	"""Ice cream restaurant that inherits from Restaurant class."""

	def __init__(self, restaurant_name, cuisine_type):
		"""
		Initialize attributes of the parent class.
		Then intialize attributes specific to an ice cream stand.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def display_flavors(self):
		"""Stores a list of ice cream flavors."""
		print("\nFlavors: ")
		for flavor in self.flavors:
			print("- " + flavor.title())

ice_cream_stand_1 = IceScreamStand('baskin robbins', 'ice cream parlor')

ice_cream_stand_1.flavors = [
	'chocolate',
	'mint chocolate chip',
	'cookie dough'
	]

ice_cream_stand_1.describe_restaurant()
ice_cream_stand_1.display_flavors()


#Admin: 9-7 & 9-8: Privileges:

class User():
	"""A User class."""

	def __init__(self, first_name, last_name, age, hometown, birthplace):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hometown = hometown
		self.login_attempts = 0
		self.birthplace = birthplace

	def describe_user(self):
		"""Prints a summary of the user's information."""

		#full_name = (self.first_name + self.middle_name + self.last_name)

		#print("Name: " + self.full_name.title())
		print("\nName: " + (self.first_name + " " + self.last_name).title())
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


class Admin(User):
	"""Admin class with User attributes."""
	
	def __init__(self, first_name, last_name, age, hometown, birthplace):
		"""
		Initialize attributes of the parent class.
		Then intialize attributes specific to the Admin user.
		"""
		super().__init__(first_name, last_name, age, hometown, birthplace)
		#self.privileges = []
		self.privileges = Privileges()

#	def show_privileges(self):
#		"""Specific Admin priveleges."""
#		print("\nAdmin Privileges: ")
#		for privilege in self.privileges:
#			print("- " + privilege)

#user_3 = Admin('dan', 'king', str(24), 'berkeley', 'san diego')

#user_3.privileges = ['Add post.', 'Delete post.', 'Ban user.',]

#user_3.describe_user()
#user_3.greet_user()
#user_3.show_privileges()


class Privileges():
	"""Seperate Privileges Class."""

	def __init__(self, privileges=[]): #Looked up.
		self.privileges = privileges

	def show_privileges(self):
		print("\nAdmin Privileges: ")
		for privilege in self.privileges:
			print("- " + privilege)

	#def show_privileges(self):
	#	print("Privileges: ")
	#	if self.privileges:
	#		for privilege in self.privileges:
	#			print("- " + privilege)

user_3 = Admin('dan', 'king', str(24), 'berkeley', 'san diego')
user_3.describe_user()

user_3_privileges = ['Add post.', 'Delete post.', 'Ban user.',]

user_3.privileges.privileges = user_3_privileges

user_3.privileges.show_privileges()


#Battery Upgrade: 9-10: 

class Car():
	"""A simple car representation."""

	def __init__(self, make, model, year):
		"""Initialize attributes/variables"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_description(self):
		"""Return description of car."""
		full_description = str(self.year) + " " + self.make + " " + self.model
		return full_description.title()

	def read_odometer(self):
		"""Show the car's mileage."""
		print("Mileage: " + str(self.odometer_reading))

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.

		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles


#Battery Class:

class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size	#Instance.

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kwh battery.")

	def get_range(self):
		"""Print a statment about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "\nThis car can go approximately " + str(range)
		message += " miles on a charge."
		print(message)

	def upgrade_battery(self):
		"""Checks the battery size and sets the capacity to 85."""
		if self.battery_size < 85 or self.battery_size > 85:
			self.battery_size = 85


#Electric Car (Child Class):

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then intialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2017)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()