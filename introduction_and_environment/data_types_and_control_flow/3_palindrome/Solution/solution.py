#Completed

# Code your solution here

## Motivation
# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromic words.

# ## Problem Description
# Write a Python script that asks the user for a string value and store this in an variable called `word`.
# Your goal is to check whether `word` is a palindrome or not. Create a variable `is_palindrome` 
# and set this value to be the boolean value `True` if `word` was a palindrome and `False` otherwise.



# word = input("enter string: ")
word = "racecar"

if word == word[::-1]:
    is_palindrome = True
else: is_palindrome = False

print(is_palindrome)