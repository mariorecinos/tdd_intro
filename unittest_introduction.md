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

## 2: Create a TestRunner Class
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

<br>
