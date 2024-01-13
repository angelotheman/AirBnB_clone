#!/usr/bin/python3

"""
Test for the review class
"""
import unittest
from models.review import review

class TestReview(unittest.TestCase):
	
	def test_default_values(self):
		user = User()
		self.assertEqual(User.place_id, "")
		self.assertEqual(User.user_id, "")
		self.assertEqual(User.text, "")

	
	if __name__ == '__main__':
		unittest.main()
