#!/usr/bin/python3
"""
Test for the console module
"""
import unittest
from unittest.mock import patch
from io import StringIO
import console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test for the entire console file
    """

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expect_output, mock_stdout):
        HBNBCommand().onecmd(expect_output)
        self.assertEqual(mock_stdout.getvalue().strip(), expect_output.strip())

    def test_quit(self):
        """
        Tests the quit function
        """
        self.assert_stdout('', 'quit\n')

    def test_EOF(self):
        """
        Tests the EOF function
        """
        self.assert_stdout('', 'EOF\n')
