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

    def test_default_values(self):
        """
        Test when an instance is created
        """

        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
