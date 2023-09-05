from unittest_demo import TestCase, TestRunner  # Import your custom TestCase and TestRunner
from main import is_palindrome # Import your is_palindrome function from main.py

class TestIsPalindrome(TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_valid_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_invalid_input(self):
         # Define a function that should raise a ValueError
        def invalid_input():
            is_palindrome("apple")

        self.assertRaises(ValueError, invalid_input,"Expected ValueError for non-string input")

if __name__ == "__main__":
    test_runner = TestRunner()
    test_case = TestIsPalindrome()

    # Run the tests
    test_runner.run(test_case)

    # Print test results
    print(f"Tests Passed: {test_case.passed}")
    print(f"Tests Failed: {test_case.failed}")
