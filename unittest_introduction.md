# Chapter 2: Building a Custom Testing Framework

<p>
In this chapter, we'll refactor our testing code to build a custom testing framework that emulates the functionality of the unittest library. We'll also develop a test runner to execute our tests. Test frameworks, like the one we'll construct, play a fundamental role in software testing. They offer a structured approach for organizing and running tests, simplifying the assessment of code correctness. By encapsulating test cases within classes and embracing object-oriented programming (OOP) principles, we establish a modular and maintainable testing methodology. This not only streamlines test development but also promotes scalability, enabling our test suite to seamlessly grow alongside our project's complexity. Creating our own testing framework will provide valuable insights into module importation, class inheritance, and the inner workings of these essential tools.
</p>

## 1.Create a TestCase Class:

Let's start by creating a ***TestCase** class that defines the structure for our individual test cases. Each test case should have a method representing a specific test.

```python3
class TestCase:
     # __init__(self) This method is the constructor of the TestCase class.
    def __init__(self):
        # are instance variables used to keep track of the number of test cases that pass and fail, respectively.
        # self.passed is initialized to 0, indicating that no tests have passed yet.
        # self.passed is initialized to 0, indicating that no tests have failed yet.
        self.passed = 0
        self.failed = 0

    def assertTrue(self, expr, msg=None):
        # This method is used to assert that a given expression, expr, is True.
        # expr: The expression that should evaluate to True.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If expr is True, it increments the self.passed counter.
        # If expr is False, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if expr:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print("AssertionError")

    def assertFalse(self, expr, msg=None):
        # This method is used to assert that a given expression, expr, is False.
        # expr: The expression that should evaluate to False.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # It internally calls assertTrue with the negation of expr to check if it's True.
        # If expr is False, it increments the self.passed counter.
        # If expr is True, it increments the self.failed counter and prints an error message.
        self.assertTrue(not expr, msg)

    def assertRaises(self, exc_type, func, *args, **kwargs):
        # This method is used to assert that a specific exception of type exc_type is raised when calling the provided function func with specified arguments.
        # exc_type: The expected exception type (e.g., ValueError, TypeError).
        # func: The function to be tested.
        # args and **kwargs: Additional arguments to pass to func.
        # If the expected exception (exc_type) is raised during the execution of func, it increments the self.passed counter.
        # If an unexpected exception is raised, it increments the self.failed counter and prints an error message indicating the expected exception and the actual exception raised.
        # If no exception is raised, it increments the self.failed counter and prints an error message indicating that no exception was raised.
        try:
            func(*args, **kwargs)
        except exc_type as e:
            self.passed += 1
        except Exception as e:
            self.failed += 1
            print(f"AssertionError: Expected {exc_type}, but got {type(e).__name__}: {e}")
        else:
            self.failed += 1
            print(f"You did not raise a {exc_type.__name__} exception. Failing Test: test_{func.__name__}")
```

The TestCase class includes assertion methods like assertTrue, assertFalse, assertRaises, and others. These methods perform assertions based on their names, such as checking if a given expression is true or false.

This TestCase class provides a comprehensive set of assertion methods that can be used to build and run test cases in a custom testing framework. It allows developers to define test cases and assert expected behaviors within their code. The class keeps track of the number of passed and failed tests, providing valuable feedback during testing and debugging.

Take a moment to review and learn about other assertion methods and other features that can be added to TestCase, you can refer to the [unittest documentation](https://docs.python.org/3/library/unittest.html#)

## 2. Create a TestRunner Class
The TestRunner class is responsible for discovering and executing test methods within a TestCase subclass.

```python3
class TestRunner:
    def run(self, test_case):
        for name in dir(test_case):
            if name.startswith("test_"):
                test_method = getattr(test_case, name)
                test_method()
```


* class TestRunner:: This code defines a Python class named TestRunner. This class is responsible for running the test methods defined within a TestCase subclass.

* def run(self, test_case):: Inside the TestRunner class, there is a method called run. This method takes two parameters: self (a reference to the instance of the class) and test_case (an instance of a TestCase subclass that contains the test methods to be executed).

* for name in dir(test_case):: This line initiates a loop that iterates through all the attributes (including methods) of the test_case object. dir(test_case) returns a list of all the attributes in test_case.

* if name.startswith("test_"):: Within the loop, it checks if the attribute name starts with the prefix "test_". In Python convention, test methods are often named with a prefix like "test_" to distinguish them from other methods.

* test_method = getattr(test_case, name): If the attribute name starts with "test_", it retrieves the method object associated with that attribute using the getattr function. This allows us to access and call the test method dynamically.

* test_method(): Finally, it calls the test method using parentheses (). This is where the actual execution of the test method takes place.

<p>
So, this TestRunner class provides a way to automatically discover and execute all the test methods within a TestCase subclass. It loops through the attributes of the TestCase object, identifies the test methods by their names (starting with "test_"), and executes them one by one. The result of running each test method is printed, including any assertion failures or errors.
</p>

This is a key part of building a custom testing framework, as it allows you to automate the execution of test cases and collect the results.

<details>

<summary> completed code </summary>

  ```python3
  class TestCase:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def assertTrue(self, expr, msg=None):
        if expr:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print("AssertionError")

    def assertFalse(self, expr, msg=None):
        self.assertTrue(not expr, msg)

    def assertRaises(self, exc_type, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except exc_type as e:
            self.passed += 1
        except Exception as e:
            self.failed += 1
            print(f"AssertionError: Expected {exc_type}, but got {type(e).__name__}: {e}")
        else:
            self.failed += 1
            print(f"You did not raise a {exc_type.__name__} exception. Failing Test: test_{func.__name__}")

  class TestRunner:
    def run(self, test_case):
        for name in dir(test_case):
            if name.startswith("test_"):
                test_method = getattr(test_case, name)
                test_method()
  ```
</details>

## 3. Using The Custom Testing Framework

1. Define a TestCase subclass that contains your test methods. Each test method should start with "test_."

2. Implement your test methods within the TestCase subclass, using the assertion methods provided by the framework (e.g., assertTrue, assertRaises, etc.).

3. Instantiate a TestRunner object and a TestCase object for your specific test suite.

4. Run the tests using test_runner.run(test_case).

5. Print the test results to see how many tests passed and how many failed.

By following these steps, you can easily create and execute test cases for your code.

<p>
In the provided example, the TestIsPalindrome class demonstrates how to create test methods using the custom testing framework. You can replace it with your own TestCase subclass and test methods.
</p>

```python3
# Import custom testing framework components
from unittest_demo import TestCase, TestRunner  # Import your custom TestCase and TestRunner
from main import is_palindrome  # Import your is_palindrome function from main.py

# Define a test case class that inherits from TestCase
class TestIsPalindrome(TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("racecarw"),  "Failing Test: Expected 'racecar' to be a palindrome")

    def test_valid_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panamaw"),  "Failing Test: Expected 'A man a plan a canal Panama' to be a palindrome")

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"), "Failing Test: Expected 'hello' not to be a palindrome")

    def test_invalid_input(self):
         # Define a function that should raise a ValueError
        def invalid_input():
            is_palindrome(123)

        # Use assertRaises to test if the function raises the expected exception
        self.assertRaises(ValueError, invalid_input)

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Create an instance of the TestRunner
    test_runner = TestRunner()

    # Create an instance of the TestIsPalindrome test case
    test_case = TestIsPalindrome()

    # Run the tests in the test case using the test runner
    test_runner.run(test_case)

    # Print test results
    print(f"Tests Passed: {test_case.passed}")
    print(f"Tests Failed: {test_case.failed}")
```

1. Custom Testing Framework Components Import: In this section, we import the custom testing framework components you've built. These components include TestCase and TestRunner from the unittest_demo module. Additionally, we import the is_palindrome function from a module named main.py, which presumably contains your application code to be tested.

2. Define Test Case Class: We define a custom test case class called TestIsPalindrome that inherits from your TestCase class. This custom test case class contains individual test methods, each beginning with the prefix "test_". These test methods contain various assertions to test different aspects of the is_palindrome function.

3. Main Program Check: The if __name__ == "__main__": block ensures that the code within it is only executed if the script is run as the main program (not when it's imported as a module).

4. Test Runner and Test Case Creation: We create instances of the TestRunner and TestIsPalindrome classes. The TestRunner is responsible for executing the test methods in the test case.

5. Run Tests: We use test_runner.run(test_case) to run all the test methods within the TestIsPalindrome test case.

6. Print Test Results: Finally, we print the number of tests that passed and failed to provide feedback to the user.

Now we can run our test in the terminal run the command
<br>
```python3
python3 test.py
```
<br>

![passing](https://user-images.githubusercontent.com/24584526/266596099-41a9bc01-9679-4c20-a746-c0a8ffe3aecb.png)

## Section 4: Using the unittest Framework
<p>
One of the key advantages of Python is its extensive ecosystem of libraries and frameworks that simplify various aspects of software development. In the context of testing, Python's built-in unittest framework offers a comprehensive solution for writing and executing test cases. Using unittest, you can efficiently organize your tests, make assertions about your code's behavior, and generate detailed test reports. This section demonstrates how to harness the power of unittest to create and run tests seamlessly.
</p>

Below is an example of how to create and run tests using the unittest framework. We'll use a test file named unittest_test.py for demonstration:

```python3
import unittest
from main import is_palindrome  # Import the function to be tested

# Create a test class that inherits from unittest.TestCase
class TestPalindrome(unittest.TestCase):

    # Test whether is_palindrome correctly identifies a palindrome
    def test_is_palindrome_positive(self):
        self.assertEqual(is_palindrome("racecar"), True)

    # Test whether is_palindrome correctly identifies a non-palindrome
    def test_is_palindrome_negative(self):
        self.assertEqual(is_palindrome("hello"), False)

    # Test whether is_palindrome correctly handles palindromes with spaces
    def test_is_palindrome_with_spaces(self):
        self.assertEqual(is_palindrome("A man a plan a canal Panama"), True)

    # Test whether is_palindrome correctly handles an empty string
    def test_is_palindrome_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

    # Another way to assert True for palindrome
    def test_is_palindrome_passes(self):
        self.assertTrue(is_palindrome("racecar"))

    # Another way to assert False for non-palindrome
    def test_is_palindrome_fails(self):
        self.assertFalse(is_palindrome("hello"))

    # Another way to assert True for palindrome with spaces
    def test_is_palindrome_with_spaces_in_word(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    # Another way to assert True for an empty string
    def test_is_palindrome_empty_string_nothing(self):
        self.assertTrue(is_palindrome(""))

    # Test input validation: Ensure is_palindrome raises a ValueError for non-string input
    def test_input_not_string(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)  # Passing an integer, should raise ValueError

# If this script is run as the main program, execute the tests
if __name__ == '__main__':
    unittest.main()
```

**Explanation:**
<br>
In this section, we demonstrate how to use the unittest framework to create and run tests for the is_palindrome function. Here's a breakdown of the key components:

* Test Class: We create a test class TestPalindrome that inherits from unittest.TestCase. Each test method is a Python function within this class.

* Test Methods: Each test method is named with a prefix test_ and is responsible for testing a specific aspect of the is_palindrome function. We use various assert methods provided by unittest.TestCase to make assertions about the function's behavior.

* Test Input Validation: We also test input validation by using self.assertRaises to ensure that the function raises a ValueError when given non-string input (e.g., an integer).

* Test Runner: The script checks if it is being run as the main program (if __name__ == '__main__':) and, if so, executes the tests using unittest.main().

To run the tests in the unittest_test.py file, execute the following command in the shell:
```python3
python3 -m unittest_test.py
```
This command uses the unittest test discovery mechanism to find and run the tests in the specified file.

<br>

![unittest_pass](https://user-images.githubusercontent.com/24584526/266599960-2b16ecc9-9b7e-4c5f-ab3d-01b43d705300.png)

