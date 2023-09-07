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
            self.assertFalse(True, f"You did not raise a {exc_type.__name__} exception. Failing Test: test_{func.__name__}")
        except exc_type:
            self.passed += 1
        except Exception as e:
            self.failed += 1
            print(f"AssertionError: Expected {exc_type}, but got {type(e).__name__}: {e}")

    def assertNotIsInstance(self, obj, cls, msg=None):
        if not isinstance(obj, cls):
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: {obj} is an instance of {cls}")

    def assertIsInstance(self, obj, cls, msg=None):
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
        if first == second:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: Expected {second}, but got {first}")

    def assertNotEqual(self, first, second, msg=None):
        if first != second:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print(f"AssertionError: Expected values to be not equal: {first} and {second}")

    def assertIn(self, member, container, msg=None):
        if member in container:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print("AssertionError")

    def assertNotIn(self, member, container, msg=None):
        if member not in container:
            self.passed += 1
        else:
            self.failed += 1
            if msg:
                print(f"AssertionError: {msg}")
            else:
                print("AssertionError")

class TestRunner:
    def run(self, test_case):
        for name in dir(test_case):
            if name.startswith("test_"):
                test_method = getattr(test_case, name)
                try:
                    test_method()
                except Exception as e:
                    print(f"Test {name} failed: {e}")

if __name__ == "__main__":
    test_runner = TestRunner()
    test_case = TestCase()

    # Run the tests
    test_runner.run(test_case)

    # Print test results
    print(f"Tests Passed: {test_case.passed}")
    print(f"Tests Failed: {test_case.failed}")
