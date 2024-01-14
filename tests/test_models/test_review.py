#!/usr/bin/python3

"""
Test for the review class
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
	
	def test_default_values(self):
		review = Review()
		self.assertTrue(hasattr(review, 'place_id'))
		self.assertTrue(hasattr(review, 'user_id'))
		self.assertTrue(hasattr(review, 'text'))
		
		
		self.assertEqual(review.place_id, "")
		self.assertEqual(review.user_id, "")
		self.assertEqual(review.text, "")

	
	if __name__ == '__main__':
		unittest.main()
