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

    def setUp(self):
        """
        set up test class for all
        """
        self.held_output = StringIO()

    def tearDown(self):
        """
        releases memory after every test
        """
        self.held_output.close()

    def assert_stdout(self, expected_output, mock_stdout):
        with patch('sys.stdout', new=self.held_output):
            HBNBCommand().onecmd(expect_output)
            self.assertEqual(
                    self.held_output.getvalue().strip(),
                    expected_output
                )

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

    def test_help(self):
        """
        Tests the help function
        """
        self.assert_stdout('', 'help\n')

    def test_empty_line(self):
        """
        Tests when nothing is entered or an empty line encountered
        """
        self.assert_stdout('', '\n')


if __name__ == '__main__':
    unittest.main()
