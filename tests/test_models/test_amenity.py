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
    def test_amenity_attributes(self):
        """
        This tests for the attributes
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
