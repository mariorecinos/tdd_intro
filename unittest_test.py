import unittest
from main import is_palindrome

# to run the test file run the command python -m unittest unittest_test.py in the shell
#  Link to documentation https://docs.python.org/3/library/unittest.html

class TestPalindrome(unittest.TestCase):

    def test_is_palindrome_positive(self):
        self.assertEqual(is_palindrome("racecarw"), True)

    def test_is_palindrome_negative(self):
        self.assertEqual(is_palindrome("hello"), False)

    def test_is_palindrome_with_spaces(self):
        self.assertEqual(is_palindrome("A man a plan a canal Panama"), True)

    def test_is_palindrome_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

#  another way is to assert with True or False

    def test_is_palindrome_passes(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_fails(self):
        self.assertFalse(is_palindrome("hello"))

    def test_is_palindrome_with_spaces_in_word(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_is_palindrome_empty_string_nothing(self):
        self.assertTrue(is_palindrome(""))

    def test_input_not_string(self):
        # Test that is_palindrome raises a ValueError when input is not a string
        with self.assertRaises(ValueError):
            is_palindrome(123)  # Passing an integer, should raise ValueError
