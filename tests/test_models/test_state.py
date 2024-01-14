#!/usr/bin/python3
"""
Tests for state class
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
	def Test_state_attributes(self):
		"""
		Test for when an instance is created
		"""
		
		state = State()
		self.assertTrue(hasattr(state, 'name'))
		self.assertEqual(state.name, "")

	if __name__ == '__main__':
		unittest.main()
