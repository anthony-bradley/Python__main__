import unittest

from name_function import get_formatted_name

#python3 test_name_function.py

class NamesTestCase(unittest.TestCase):
	"""Tests for name_function.py"""

	def test_first_last_name(self):
		"""Tests first and last names."""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Tests first, last, and middle names."""
		formatted_name = get_formatted_name(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()