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

## Task:
You will implement a function called is_palindrome that checks if a given input string is a palindrome. A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward, ignoring spaces and considering letters in a case-insensitive manner.

## Function Signature:
```python3

def is_palindrome(input_string):
    Check if a given input string is a palindrome.

    Parameters:
    input_string (str): The string to be checked for palindrome.

    Returns:
    bool: True if the input string is a palindrome, False otherwise.

    Raises:
    ValueError: If the input is not a string.
```
