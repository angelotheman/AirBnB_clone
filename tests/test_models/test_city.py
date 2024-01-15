#!/usr/bin/python3
"""
Test for city class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    The test for the class method
    """
    def test_city_attributes(self):
        """
        Test for checking the attribute instance
        """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")


if __name__ == '__main__':
    unittest.main()
