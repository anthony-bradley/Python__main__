"""
Module.
Classes: Restaurant
"""

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