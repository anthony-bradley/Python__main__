class Employee():
	"""Employee Class."""

	def __init__(self, first_name, last_name, salary):
		"""Attributes."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.salary = salary

	def give_raise(self, bonus=5000):
		"""Adds $5,000 to annual salary."""
		self.salary += bonus