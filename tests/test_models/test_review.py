#!/usr/bin/python3
"""
Module for testing the review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    This tests for the Review class methods
    """

    def setUp(self):
        """
        Initialiazation of the class for all functions
        """
        review = Review()

    def test_attributes(self):
        """
        Testing the various attributes of the class
        """
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_values(self):
        """
        Tests default values when the class is instantiated
        """
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_instances(self):
        """
        Tests the various class types of all the attributes
        """
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == '__main__':
    unittest.main()
