# Check if a given input string is a palindrome.
# Parameters:
# input_string (str): The string to be checked for palindrome.
# Returns:
# bool: True if the input string is a palindrome, False otherwise.
# Raises:
# ValueError: If the input is not a string.

#A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
#ignoring spaces and considering letters in a case-insensitive manner.
# Example:
#>>> is_palindrome("racecar")
#True
#>>> is_palindrome("A man a plan a canal Panama")
#True
#>>> is_palindrome("hello")
#False
# One approach is we can take our string and print values using [] to get the index.
# original_string = "racecar"
# this should printout r
# print(original_string[0])
# we then can compare if the first value and the next value are the same usng the comparison operator
# print(original_string[0] == original_string[6])  # >>> True
# we can do this for every single value until the beginning and ending values meet each other
# print(original_string[1] == original_string[5]) # >>> True
# print(original_string[2] == original_string[4]) # >>> True
# print(original_string[3] == original_string[3]) # >>> True

# We have walked through our approach to solving this problem we will now take a more dynamic approach
# that can be scaled to strings of different lengths without us having to manually compare each value.

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

# Function to test if a given string is a palindrome.
# Takes an input string, checks if it is a palindrome using the is_palindrome function,
# and returns a pass/fail indication based on the result.
# If the string is a palindrome, returns "Test Passed ✅",

def test_palindrome(input_string, expected_result):
    result = is_palindrome(input_string)
    if result == expected_result:
        return "Test Passed ✅"
    else:
        return "Test Failed ❌"

# Check if a valid palindrome is identified correctly
# print(test_palindrome("racecar", True))  # Should print "Test Passed ✅"

# Check if a valid palindrome with spaces is identified correctly
# print(test_palindrome("A man a plan a canal Panama", True))  # Should print "Test Passed ✅"

# Check if a non-palindrome is identified correctly
# print(test_palindrome("hello", False))  # Should print "Test Passed ✅"

# Check if invalid input raises a ValueError
# print(test_palindrome(123, False))  # Should print raise ValueError("Input must be a string") ValueError: Input must be a string


# def test_add(num1, num2, expected_result):
#     result = add(num1, num2)
#     if result == expected_result:
#         return "Test Passed ✅"
#     else:
#         return "Test Failed ❌"

# Define the add function
# def add(a, b):
#     return a + b

# Run the test cases
# print(test_add(2, 3, 5))      # Test Passed ✅
# print(test_add(5, -3, 2))     # Test Passed ✅
# print(test_add(-7, -2, -9))   # Test Passed ✅
# print(test_add(0, 8, 8))      # Test Passed ✅
