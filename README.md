# Lesson: Introduction to Test-Driven Development (TDD)<br>

## Goal:<br>
In this lesson, you will learn the fundamentals of Test-Driven Development (TDD) by tackling the is_palindrome coding challenge. We will start by identifying the goal of our function, writing tests for it, and then implementing the function to make the tests pass.

## What is Test-Driven Development (TDD)?

Test-Driven Development (TDD) is a software development methodology where you write tests before you write the actual code. The primary steps of TDD are:

1. Write a Test: You start by writing a test that defines what the code should do. This test initially fails because there's no code to make it pass.

2. Write the Code: You then write the minimum code necessary to make the test pass. The goal is to make the test pass, not to write the complete functionality.

3. Run the Tests: You run all your tests, including the new one. If any test fails, you refine the code until all tests pass.

4. Refactor: Once all tests pass, you can refactor your code for readability, performance, and maintainability, while keeping all tests passing.

## Your First TDD Assignment: is_palindrome

### Task:
You will implement a function called is_palindrome that checks if a given input string is a palindrome. A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward, ignoring spaces and considering letters in a case-insensitive manner.

### Function Signature:
```python3

def is_palindrome(input_string):
    Check if a given input string is a palindrome.

    Parameters:
    input_string (str): The string to be checked for palindrome.

    Returns:
    bool: True if the input string is a palindrome, False otherwise.

    Raises:
    ValueError: If the input is not a string.

#A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
#ignoring spaces and considering letters in a case-insensitive manner.
# Example:
#>>> is_palindrome("racecar")
#Output True
#>>> is_palindrome("A man a plan a canal Panama")
#Output True
#>>> is_palindrome("hello")
#Output False
```

## Test-First Approach:

We will begin with a test-first approach. Before writing the is_palindrome function, let's write tests to define how it should behave.  Before writing the test let's take a moment to discuss how is our code supposed to behave what input are we receiving and what is the output?
<br><br>
We'll start with a simple test function called
### test_palindrome:
```python3
def test_palindrome(input_string, expected_result):
    result = is_palindrome(input_string)
    if result == expected_result:
        return "Test Passed ✅"
    else:
        return "Test Failed ❌"
```

This **test_palindrome** function takes an **input_string** and the **expected_result**. It checks if calling **is_palindrome(input_string)** matches the expected_result. If they match, the test passes; otherwise, it fails.

### Example Tests:

Let's write some example tests for the **is_palindrome** function:
```python3
# Check if a valid palindrome is identified correctly
print(test_palindrome("racecar", True))  # Should print "Test Passed ✅"

# Check if a valid palindrome with spaces is identified correctly
print(test_palindrome("A man a plan a canal Panama", True))  # Should print "Test Passed ✅"

# Check if a non-palindrome is identified correctly
print(test_palindrome("hello", False))  # Should print "Test Passed ✅"

# Check if invalid input raises a ValueError
print(test_palindrome(123, None))  # Should print "Test Failed ❌"
```

Let's try to run our test in the terminal run the command:
```python3
python3 main.py
```

We should receive a print statement in the terminal showing that all of our test have failed. Since we have no logic in our is_palindrome function.<br><br>
![Test_Failing](https://user-images.githubusercontent.com/24584526/265599428-c3bc45a0-b9ff-4a90-9a3f-38f21b459b36.png)


In this example, we've defined the behavior we expect from the is_palindrome function using these tests. Your task is to complete the is_palindrome function to make these tests pass. Remember, TDD encourages incremental development, so start with the simplest code that makes the first test pass, and then move on to the next.
we will split up into breakout rooms in pairs and work on writing the code for our is_palindrome function in order for the test to pass.
in order to run the code in your text editor run the command
```python3
python3 main.py
```

your **main.py** file should look like this
```python3
def is_palindrome(input_string):
    #Check if a given input string is a palindrome.

    #Parameters:
    #input_string (str): The string to be checked for palindrome.

    #Returns:
    #bool: True if the input string is a palindrome, False otherwise.

    #Raises:
    #ValueError: If the input is not a string.

#A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
#ignoring spaces and considering letters in a case-insensitive manner.
# Example:
#>>> is_palindrome("racecar")
#Output True
#>>> is_palindrome("A man a plan a canal Panama")
#Output True
#>>> is_palindrome("hello")
#Output False

def test_palindrome(input_string, expected_result):
    result = is_palindrome(input_string)
    if result == expected_result:
        return "Test Passed ✅"
    else:
        return "Test Failed ❌"


# Check if a valid palindrome is identified correctly
print(test_palindrome("racecar", True))  # Should print "Test Passed ✅"

# Check if a valid palindrome with spaces is identified correctly
print(test_palindrome("A man a plan a canal Panama", True))  # Should print "Test Passed ✅"

# Check if a non-palindrome is identified correctly
print(test_palindrome("hello", False))  # Should print "Test Passed ✅"

# Check if invalid input raises a ValueError
print(test_palindrome(123, None))  # Should print "Test Failed ❌"

```
