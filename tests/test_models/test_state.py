#!/usr/bin/python3
"""
Tests for state class
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
	def Test_state_values(self):
		"""
		Test for when an instance is created
		"""
		
		user = User()
		
		self.assertEqual(User.name, "")

	if __name__ == '__main__':
		unittest.main()
