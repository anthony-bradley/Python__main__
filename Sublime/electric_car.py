#python3 electric_car.py

#Car Class:

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

		message = "This car can go approximately " + str(range)
		message += " miles on a charge."
		print(message)


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

	#def describe_battery(self):
	#	"""Print a statement describing the battery size."""
	#	print("This car has a " + str(self.battery_size) + " -kwh battery.")

	#def fill_gas_tank(self):
	#	"""Electric cars don't have gas tanks."""
	#	print("This car doesn't need a gas tank!")

#my_tesla.describe_battery()
#my_tesla.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', '2017')

print(my_tesla.get_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() 