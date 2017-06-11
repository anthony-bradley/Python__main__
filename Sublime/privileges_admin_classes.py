"""
Classes: Admin, Priviliges
Imported: User 
"""

from user_class import User

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


class Privileges():
	"""Seperate Privileges Class."""

	def __init__(self, privileges=[]): #Looked up.
		self.privileges = privileges

	def show_privileges(self):
		print("\nAdmin Privileges: ")
		for privilege in self.privileges:
			print("- " + privilege)