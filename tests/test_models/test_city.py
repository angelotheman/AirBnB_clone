#!/usr/bin/python3
"""
Test for city class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):

	def test_city_attributes(self):
		city = City()
		self.assertTrue(hasattr(city, 'state_id'))
		self.assertTrue(hasattr(city, 'name'))
		self.assertEqual(city.state_id, "")
	
if __name__ == '__main__':
	unittest.main()
