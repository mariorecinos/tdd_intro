# Chapter 2: Building a Custom Testing Framework

<p>
In this chapter, we'll refactor our testing code to build a custom testing framework that emulates the functionality of the unittest library. We'll also develop a test runner to execute our tests. Test frameworks, like the one we'll construct, play a fundamental role in software testing. They offer a structured approach for organizing and running tests, simplifying the assessment of code correctness. By encapsulating test cases within classes and embracing object-oriented programming (OOP) principles, we establish a modular and maintainable testing methodology. This not only streamlines test development but also promotes scalability, enabling our test suite to seamlessly grow alongside our project's complexity. Creating our own testing framework will provide valuable insights into module importation, class inheritance, and the inner workings of these essential tools.
</p>

## 1.Create a TestCase Class:

Let's start by creating a ***TestCase** class that defines the structure for our individual test cases. Each test case should have a method representing a specific test.

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
            self.assertFalse(True, f"Expected {exc_type}, but no exception raised")
        except exc_type:
            self.passed += 1
        except Exception as e:
            self.failed += 1
            print(f"AssertionError: Expected {exc_type}, but got {type(e).__name__}: {e}")

```
