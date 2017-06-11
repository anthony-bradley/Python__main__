#python3 car_class.py

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


car_1 = Car('audi', 'r8', 2017)
print(car_1.get_description())

#car_1.odometer_reading = 1000
#car_1.read_odometer()


car_1.update_odometer(1000)
car_1.read_odometer()


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_description())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()