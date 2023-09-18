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

create a new file called **test.py** and inside you should have:

```python3
# Import custom testing framework components
from unittest_demo import TestCase, TestRunner  # Import your custom TestCase and TestRunner
from main import is_palindrome  # Import your is_palindrome function from main.py

# Define a test case class that inherits from TestCase
class TestIsPalindrome(TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("racecar"),  "Failing Test: Expected 'racecar' to be a palindrome")

    def test_valid_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"),  "Failing Test: Expected 'A man a plan a canal Panama' to be a palindrome")

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

1. **Custom Testing Framework Components Import:** In this section, we import the custom testing framework components you've built. These components include TestCase and TestRunner from the unittest_demo module. Additionally, we import the is_palindrome function from a module named main.py, which presumably contains your application code to be tested.

2. **Define Test Case Class:** We define a custom test case class called TestIsPalindrome that inherits from your TestCase class. This custom test case class contains individual test methods, each beginning with the prefix "test_". These test methods contain various assertions to test different aspects of the is_palindrome function.

3. **Main Program Check:** The if __name__ == "__main__": block ensures that the code within it is only executed if the script is run as the main program (not when it's imported as a module).

4. **Test Runner and Test Case Creation:** We create instances of the TestRunner and TestIsPalindrome classes. The TestRunner is responsible for executing the test methods in the test case.

5. **Run Tests:** We use test_runner.run(test_case) to run all the test methods within the TestIsPalindrome test case.

6. **Print Test Results:** Finally, we print the number of tests that passed and failed to provide feedback to the user.

Now we can run our test in the terminal run the command:
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

Below is an example of how to create and run tests using the unittest framework. We'll use a test file named **unittest_test.py** for demonstration:

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
```

**Explanation:**
<br>

In this section, we demonstrate how to use the unittest framework to create and run tests for the **is_palindrome function**. Here's a breakdown of the key components:

* **Test Class:** We create a test class TestPalindrome that inherits from unittest.TestCase. Each test method is a Python function within this class.

* **Test Methods:** Each test method is named with a prefix test_ and is responsible for testing a specific aspect of the is_palindrome function. We use various assert methods provided by unittest.TestCase to make assertions about the function's behavior.

To run the tests in the unittest_test.py file, execute the following command in the shell:
```python3
python3 -m unittest_test.py
```
This command uses the unittest test discovery mechanism to find and run the tests in the specified file.

<br>

![unittest_pass](https://user-images.githubusercontent.com/24584526/266599960-2b16ecc9-9b7e-4c5f-ab3d-01b43d705300.png)
<br>

## Section 5: Understanding Code Coverage
<p>
Code coverage is a critical aspect of testing that helps you measure the effectiveness of your tests. It quantifies how much of your source code is executed by your tests. In Python, you can use the coverage library to measure code coverage.
</p>

### Why Code Coverage Matters
Code coverage serves several purposes:
<br>

1. **Identify Uncovered Code:** It helps you identify areas of your code that are not covered by tests. Uncovered code may contain bugs that go unnoticed.
2. **Assess Test Quality:** A high code coverage percentage indicates that most of your code is tested. However, it doesn't guarantee that your tests are of high quality. You need both high coverage and meaningful tests.
3. **Refactoring Confidence:** When refactoring code, having good test coverage provides confidence that you haven't introduced regressions.

### Measuring Code Coverage With Coverage Library
Let's revisit our **is_palindrome** example and measure its code coverage using the **coverage** library.

**Step 1:** Install `coverage`
<br>
```python3
pip install coverage
```

**Step 2:** Writing Tests
<br>

Ensure you have a set of tests for your code. In the case of **is_palindrome**, we already have a set of tests in the **unittest_test.py** file.
<br>

**Step 3:** Measure Code Coverage

Now, you can measure code coverage by running your tests with **coverage**. In your terminal, navigate to the project directory and execute:
<br>
```python3
coverage run -m unittest unittest_test.py
```
This command tells coverage to run your tests with the -m unittest flag.
<br>
<br>
![coverage_pass](https://user-images.githubusercontent.com/24584526/267593988-481ffe23-da44-49ec-af4c-a91b8b20f846.png)

Awesome! All of our test are passing
<br>
<br>
**Step 4: Generating A Coverage Report**<br>
After running your tests, you can generate a coverage report by running the command:
```python3
coverage report -m
```
This command generates a report that shows which lines of your code were executed during the tests and which were not. It also calculates the code coverage percentage.
<br>

**Interpreting The Coverage Report**
<br>
The coverage report provides valuable insights into your codebase:

* **Coverage Percentage:** This is the most important metric. It tells you what percentage of your code is covered by tests. Aim for high coverage, but remember that 100% coverage is not always necessary or practical.

* **Missing Lines:** The report highlights lines of code that were not executed during the tests. These are areas you should consider adding tests for.

* **Covered Lines:** Lines of code that were executed during the tests are marked as covered. This indicates that your tests exercise these parts of the code.

Here's an example coverage report for our **is_palindrome** example:
<br>

![coverage_report](https://user-images.githubusercontent.com/24584526/267596156-85275a36-1e55-4500-a81f-2bbfb47f4835.png)
<br>
In this report:

* Stmts represents the number of executable statements in each file.

* Miss indicates the number of missed lines (lines not executed).

* Cover is the coverage percentage.

* Missing shows specific lines that were not executed.

In our report it shows that line 35 is not being tested in main.py let's go ahead and review that line of code.
```python3
raise ValueError("Input must be a string")
```

It appears that we are not testing to raise the ValueError let's go ahead and include another test inside of our **unittest_test.py** file.

```python3
def test_input_not_string(self):
        # Test that is_palindrome raises a ValueError when input is not a string
        with self.assertRaises(ValueError):
            is_palindrome(123)  # Passing an integer, should raise ValueError
```
* **Objective:** This test case aims to verify that the is_palindrome function correctly raises a ValueError when provided with input that is not a string.

* **Test Process:** It uses the assertRaises context manager to check if calling the is_palindrome function with an integer (123) as input results in a ValueError being raised. The expectation is that the function should raise this specific exception when non-string input is provided.

Run our test to make sure it passes
```python3
coverage run -m unittest unittest_test.py
```
We should now have 9 test passing:
<br>

![9_test_passing](https://user-images.githubusercontent.com/24584526/267599476-cbb597da-4ea8-4e2d-8ab8-27549872f05b.png)

Now let's go ahead and get our updated coverage report run the command:
```python3
coverage report -m
```
Now we should have **100%** code coverage!
<br>
![100_coverage](https://user-images.githubusercontent.com/24584526/267600520-c34b7b54-4f0f-4015-ae91-a5c3fcf51d4b.png)
<br>

### Code Coverage In Practice
<p>
While achieving high code coverage is a good goal, it's important to prioritize writing meaningful tests that cover critical functionality and edge cases. High coverage alone does not guarantee that your code is bug-free.
</p>

Use code coverage as a tool to guide your testing efforts, identify areas that need more attention, and maintain code quality as your project grows.

<p>
By using unittest, you can benefit from a well-established testing framework without having to build your testing infrastructure from scratch, as shown in the earlier sections. This approach provides consistency and makes it easier to collaborate with others who are familiar with standard testing practices in Python.
</p>

<br>

[Implementing CI/CD with GitHub Actions](https://github.com/mariorecinos/tdd_intro/blob/main/ci_cd_intro_github_actions.md)
