"""
User class only.
"""

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
