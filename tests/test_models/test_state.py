#!/usr/bin/python3
"""
Tests for state class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Class method of all state attributes
    """

    def setup(self):
        """
        Initializes my object instance
        """
        state = State()

    def Test_attributes(self):
        self.assertTrue(hasattr(state, 'name'))

    def test_default_values(self):
        """
        Tests the default values of all the attributes
        """
        self.assertEqual(state.name, "")

    def test_attribute_instance(self):
        """
        Tests the various types of the attributes
        """
        selfassertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
