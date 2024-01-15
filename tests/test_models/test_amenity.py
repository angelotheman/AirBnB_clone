#!/usr/bin/python3
"""
Test for the Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    This tests for the Review class methods
    """
    def setUp(self):
        """
        Initializing the object instance
        """
        amenity = Amenity()

    def test_attributes(self):
        """
        This tests for the attributes
        """
        self.assertTrue(hasattr(amenity, 'name'))

    def test_default_values(self):
        """
        Test the default values of the attributes
        """
        self.assertEqual(amenity.name, "")

    def test_attribute_instance(self):
        """
        Tests an instance of the attribute
        """
        self.assertIsInstance(amenity, str)


if __name__ == '__main__':
    unittest.main()
