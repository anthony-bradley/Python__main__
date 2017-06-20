import unittest

from city_functions import city_country

#python3 test_cities.py

class CitiesTestCase(unittest.TestCase):
	"""Tests city_functions.py function."""

	def test_city_country(self):
		"""Tests 'city, country' format."""
		location = city_country('santiago', 'chile')
		self.assertEqual(location,'Santiago, Chile')

	def test_city_country(self):
		location = city_country('santiago', 'chile', 500000)
		self.assertEqual(location, 'Santiago, Chile - Population: 500000')

unittest.main()