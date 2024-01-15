#!/usr/bin/python3
"""
Tests for the user class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Testing for various components such as
    - email
    - firstname
    - password
    - lastname
    """

    def setUp(self):
        """
        Initializes my object instance
        """
        user = User()

    def test_default_values(self):
        """
        Test when an instance is created
        """
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_attributes_instance(self):
        """
        Tests the various types of attributes
        """
        self.assertIsInstance(email, str)
        self.assertIsInstance(password, str)
        self.assertIsInstanec(first_name, str)
        self.assterIsInstance(last_named, str)


if __name__ == '__main__':
    unittest.main()
