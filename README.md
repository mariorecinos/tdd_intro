# Lesson: Introduction to Test-Driven Development (TDD)<br>

## Goal:<br>
In this lesson, you will learn the fundamentals of Test-Driven Development (TDD) by tackling the is_palindrome coding challenge. We will start by identifying the goal of our function, writing tests for it, and then implementing the function to make the tests pass.  We'll explore why TDD is essential, how it can be beneficial in large-scale teams, and how to ensure maximum test coverage.

## What is Test-Driven Development (TDD)?

Test-Driven Development (TDD) is a software development methodology where you write tests before you write the actual code. The primary steps of TDD are:

1. Write a Test: You start by writing a test that defines what the code should do. This test initially fails because there's no code to make it pass.

2. Write the Code: You then write the minimum code necessary to make the test pass. The goal is to make the test pass, not to write the complete functionality.

3. Run the Tests: You run all your tests, including the new one. If any test fails, you refine the code until all tests pass.

4. Refactor: Once all tests pass, you can refactor your code for readability, performance, and maintainability, while keeping all tests passing.

## Understanding the Importance of Test-Driven Development (TDD)

### Why Test-Driven Development (TDD)?

**1.Ensuring Correctness and Reliability:**
One of the primary reasons for using TDD is to ensure that your code works correctly and reliably. By writing tests before you write the code, you have a clear specification of what the code should do. This means that when your tests pass, you can have confidence that your code behaves as expected.

**2. Guiding Development:**
TDD acts as a guide for your development process. It helps you break down complex problems into smaller, more manageable pieces. You start by writing a test for a specific piece of functionality, and then you implement just enough code to make that test pass. This iterative process helps you focus on one thing at a time, leading to cleaner and more modular code.

**3. Catching Bugs Early:**
TDD allows you to catch and fix bugs early in the development process. When you write tests, you often consider various edge cases and potential issues that might arise. This proactive approach helps you identify and address problems before they become more challenging and costly to fix.

**4. Encouraging Refactoring:**
TDD encourages refactoring, which means improving the code's structure, readability, and performance without changing its behavior. Since you have tests in place, you can confidently refactor your code, knowing that you'll quickly detect any regressions if they occur.

**5. Collaboration in Teams:**
In large-scale development teams, TDD becomes even more crucial. It provides a common language and framework for collaboration. Team members can understand the code's intended behavior through the tests and contribute to the codebase with confidence.

**6. Continuous Integration and Deployment:**
TDD fits seamlessly with continuous integration (CI) and continuous deployment (CD) practices. Automated tests created during TDD can be integrated into the CI/CD pipeline, ensuring that changes are thoroughly tested before being deployed to production environments.

**7. Maximizing Test Coverage:**
To ensure maximum test coverage, consider the following guidelines:

* Test Positive and Negative Cases: Write tests for both expected (positive) and unexpected (negative) cases. This includes testing valid inputs as well as edge cases and invalid inputs.
* Cover All Code Paths: Ensure that your tests cover all the code paths in your application. This includes branching conditions, loops, and error handling.
* Use Code Coverage Tools: Code coverage tools (Coverage.py is a tool we will use) can help identify which parts of your code are covered by tests. Aim for high code coverage, but remember that 100% coverage doesn't guarantee that your code is bug-free.
* Regularly Review and Update Tests: As your code evolves, review and update your tests to reflect the changes. This ensures that your tests remain relevant and continue to catch potential issues.
* 100% Coverage Is Not Always Necessary: While high code coverage is generally desirable, achieving 100% coverage may not always be practical or necessary. It's important to prioritize testing critical and complex code paths.

### What to Test For:
When writing tests, consider the following aspects:

* Input Validation: Test that your code handles valid inputs correctly and raises errors or exceptions for invalid inputs.
* Expected Behavior: Ensure that your code behaves as expected under various scenarios, including boundary conditions and edge cases.
* Error Handling: Test how your code handles unexpected errors and exceptions gracefully.
* Performance: In some cases, it's essential to test the performance of your code, especially for critical and resource-intensive operations.

In summary, Test-Driven Development (TDD) is a critical practice in software development that ensures correctness, guides development, catches bugs early, encourages refactoring, and supports collaboration in large teams. To achieve maximum test coverage, focus on testing both positive and negative cases, covering all code paths, using code coverage tools, and regularly updating tests to reflect code changes.

## Test-Driven Development (TDD) in Action

### Section 1: Writing the Initial Test
In this section, we'll apply the principles of Test-Driven Development (TDD) to create a simple function for adding two numbers. We'll start by writing the initial test.<br>
**Step 1: Write the Initial Test**
```python3
# Define a test function for adding two numbers with specified inputs and expected result.
def test_add():
    # Test case 1: Adding two positive numbers by calling the add function with 2 and 3 as parameters
    result = add(2, 3)
    # the expected result of invoking our function should be 5 when adding 2 + 3
    expected = 5
    # use the comparison operator to check if our result is equal to expcted
    if result == expected:
    # if true our test passes
        print("Test Passed ✅")
    else:
    # else it will fail
        print("Test Failed ❌")
# invoking our test_add function
test_add()
```
<br>
In this step, we begin by writing the first test case for our add function. We specify that adding 2 and 3 should result in 5. Running this test initially will fail because there is no add function implemented yet.<br>
<br>

![add_fail](https://user-images.githubusercontent.com/24584526/265627656-35a2c970-b67c-4528-90e1-b54e34c15e1c.png)
<br><br>
**Step 2: Write the code**
We will now include our **add** function

```python3
def test_add():
    # Test case 1: Adding two positive numbers
    result = add(2, 3)
    expected = 5
    if result == expected:
        print("Test Passed ✅")
    else:
        print("Test Failed ❌")

# Define the add function
def add(a, b):
    return a + b

test_add()
```
**Step 3: Run Test**
Now we have our **add** function that should pass our test let's give it a try in the terminal run:
```python3
python3 -m main.py
```
We should now see that our test is passing

![test_pass](https://user-images.githubusercontent.com/24584526/265629310-4222074c-8008-4abb-8cb1-2d2e2ab16d0c.png)

**Step 4: Refactor Test Code For Reusability**

In this step, we refactor our testing approach to create a more reusable and structured **test_add** function. Now, this function can be called with different inputs and expected results for multiple test cases, making it easier to manage and extend our testing suite.

```python3
# Define a test function for adding two numbers with specified inputs and expected result.
def test_add(num1, num2, expected_result):
    # Call the 'add' function with 'num1' and 'num2' as inputs and store the result in 'result'.
    result = add(num1, num2)

    # Check if 'result' is equal to the 'expected_result'.
    if result == expected_result:
        # If the result matches the expected result, print a message indicating the test passed.
        return "Test Passed ✅"
    else:
        # If the result does not match the expected result, print a message indicating the test failed.
        return "Test Failed ❌"

# Define the 'add' function, which takes two numbers ('a' and 'b') and returns their sum.
def add(a, b):
    return a + b

# Example test cases using the 'test_add' function:
print(test_add(2, 3, 5))      # Test Passed ✅
print(test_add(5, -3, 2))     # Test Passed ✅
print(test_add(-7, -2, -9))   # Test Passed ✅
print(test_add(0, 8, 8))      # Test Passed ✅
```
**Run Our Test Again**
Let's go ahead and run our test now running the command:
```python3
python3 main.py
```
Our test should be all passing now!<br><br>
![all_add_pass](https://user-images.githubusercontent.com/24584526/265633878-74cffb56-f796-4f87-8853-bde5d82bfb5c.png)



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
print(test_palindrome(123, None))  #Should print raise ValueError("Input must be a string") ValueError: Input must be a string
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

## Planning the Solution:
Before we start writing the code, let's plan our approach to solving the **is_palindrome** problem. The goal of this function is to check if a given input string is a palindrome. Here's what we need to consider:

* **Parameters:** The function should take one parameter, ***input_string***, which is the string to be checked for palindrome.
* **Return:** The function should return a boolean value (***True*** if the input string is a palindrome, ***False*** otherwise).
* Exception Handling: We should raise a ValueError if the input is not a string.
* Palindrome Definition: A palindrome is a sequence of characters that reads the same forward and backward, ignoring spaces, and considering letters in a case-insensitive manner.

### One approach to solve this problem is by using the concept of indexing and comparison. Here's how it works:

* We can access individual characters in a string using indexing. For example, for the string "racecar," original_string[0] would return 'r'.
* We can compare characters at different positions in the string using the equality operator. For instance, original_string[0] == original_string[6] would return True because both 'r' characters are equal.
* We can apply this comparison technique to every pair of characters in the string, starting from the beginning and end and moving toward the center.
* If all character pairs are equal during this comparison process, the string is a palindrome.  If they are not equal then we will return false

```python3
# One approach is we can take our string and print values using [] to get the index.
original_string = "racecar"
# this should printout r
print(original_string[0])
# we then can compare if the first value and the next value are the same usng the comparison operator
print(original_string[0] == original_string[6])  # >>> True
# we can do this for every single value until the beginning and ending values meet each other
print(original_string[1] == original_string[5]) # >>> True
print(original_string[2] == original_string[4]) # >>> True
print(original_string[3] == original_string[3]) # >>> True

# We have walked through our approach to solving this problem we will now take a more dynamic approach
# that can be scaled to strings of different lengths without us having to manually compare each value.
```
<details>

<summary>is_palindrome Completed Code</summary>

  ```python3
  def is_palindrome(input_string):
  # Check if input_string is a string using isInstance method built in python https://www.w3schools.com/python/ref_func_isinstance.asp
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(input_string.split()).lower()

    # Initialize pointers
    # our left pointer begins at 0 so that when we access the index of our string
    # the value we will be entering in the [] will be our left pointer value which will start at the beginning.
    # our right pointer will begin at the end entering the value of right pointer inside of [] will access the index of that letter value
    # then we will compare the two values to each other if they are equal if they are the left pointer will increase by one moving the next character
    #  while our right pointer will decrease by one moving down to the next value and the comparison will continue until left pointer is no longer less than right pointer
    left_pointer = 0
    right_pointer = len(cleaned_string) - 1

    # Loop until pointers meet
    while left_pointer < right_pointer:
        if cleaned_string[left_pointer] != cleaned_string[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    # If the loop completes, it's a palindrome
    return True
  ```
</details>
