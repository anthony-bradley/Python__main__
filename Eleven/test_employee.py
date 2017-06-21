#python3 test_employee.py

import unittest
from employee import Employee

class TestsEmployee(unittest.TestCase):
	"""Tests Employee Class."""

	def setUp(self):
		"""Creates an object for all test methods."""
		self.me = Employee('anthony', 'thudium', 100000)

	def test_give_default_bonus(self):
		"""Gives the default bonus amount."""
		self.me.give_raise()
		self.assertEqual(self.me.salary, 105000)

	def test_give_custom_bonus(self): 
		"""Gives a custom bonus amount."""
		self.me.give_raise(10000)
		self.assertEqual(self.me.salary, 110000)

unittest.main()