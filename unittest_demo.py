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

    def assertNotIsInstance(self, obj, cls, msg=None):
        # This method is used to assert that an object obj is not an instance of a specified class cls.
        # obj: The object to be checked.
        # cls: The class type that obj should not be an instance of.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If obj is not an instance of cls, it increments the self.passed counter.
        # If obj is an instance of cls, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if not isinstance(obj, cls):
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: {obj} is an instance of {cls}")

    def assertIsInstance(self, obj, cls, msg=None):
        # This method is used to assert that an object obj is an instance of a specified class cls.
        # obj: The object to be checked.
        # cls: The class type that obj should be an instance of.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If obj is an instance of cls, it increments the self.passed counter.
        # If obj is not an instance of cls, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if isinstance(obj, cls):
            self.passed += 1
        else:
            self.failed += 1
            expected = cls.__name__  # Get the name of the expected class
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: Expected to be an instance of {expected}, but got {type(obj).__name__}")

    def assertEqual(self, first, second, msg=None):
        # This method is used to assert that two values, first and second, are equal.
        # first: The first value for comparison.
        # second: The second value for comparison.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If first and second are equal, it increments the self.passed counter.
        # If first and second are not equal, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if first == second:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: Expected {second}, but got {first}")

    def assertNotEqual(self, first, second, msg=None):
        # This method is used to assert that two values, first and second, are not equal.
        # first: The first value for comparison.
        # second: The second value for comparison.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If first and second are not equal, it increments the self.passed counter.
        # If first and second are equal, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if first != second:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: Expected values to be not equal: {first} and {second}")

    def assertIn(self, member, container, msg=None):
        # This method is used to assert that a value member is present in a container (e.g., list, set, dictionary).
        # member: The value to check for in the container.
        # container: The container in which to search for member.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If member is found in container, it increments the self.passed counter.
        # If member is not found in container, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if member in container:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print("AssertionError")

    def assertNotIn(self, member, container, msg=None):
        # This method is used to assert that a value member is not present in a container (e.g., list, set, dictionary).
        # member: The value to check for absence in the container.
        # container: The container in which to search for member.
        # msg (optional): An optional custom error message to provide more context when the assertion fails.
        # If member is not found in container, it increments the self.passed counter.
        # If member is found in container, it increments the self.failed counter and prints an error message.
        # The error message can be customized using the msg parameter, but if not provided, a default message is used.
        if member not in container:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print("AssertionError")

class TestRunner:
    # TestRunner class, there is a method called run.
    # This method takes two parameters: self (a reference to the instance of the class) and test_case (an instance of a TestCase subclass that contains the test methods to be executed).
    # for name in dir(test_case):: This line initiates a loop that iterates through all the attributes (including methods) of the test_case object. dir(test_case) returns a list of all the attributes in test_case.
    # if name.startswith("test_"):: Within the loop, it checks if the attribute name starts with the prefix "test_". In Python convention, test methods are often named with a prefix like "test_" to distinguish them from other methods.
    # test_method = getattr(test_case, name): If the attribute name starts with "test_", it retrieves the method object associated with that attribute using the getattr function. This allows us to access and call the test method dynamically.
    # test_method(): Finally, it calls the test method using parentheses (). This is where the actual execution of the test method takes place.
    def run(self, test_case):
        for name in dir(test_case):
            if name.startswith("test_"):
                test_method = getattr(test_case, name)
                test_method()
