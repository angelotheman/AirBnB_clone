#!/usr/bin/python3
"""
Tests for the place class
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
	
	def test_place_values(self):
		user = User()
		
		self.assertEqual(User.City.id, "")
		self.assertEqual(User.User.id, "")
		self.assertEqual(User.name, "")
		self.assertEqual(User.description, "")
		self.assertEqual(User.number_rooms, "")
		self.assertEqual(User.number_bathrooms, "")
		self.assertEqual(User.max_guest, "")
		self.assertEqual(User.price_by_night, "")
		self.assertEqual(User.latitude, "")
		self.assertEqual(User.longitude, "")
		self.assertEqual(User.amenity_ids, "")
	
	if __name__ == '__main__':
		unittest.main()
