#Completed

# Code your solution here
## Problem Description
# Write a Python script that asks the user for a character as input and store this in an object called `letter`.
# Your goal is to check whether the character is a vowel or consonent. Define a variable called `result`, 
# and set this to the string `"vowel"` if the character was a vowel, and `"cosonant"` if the character was a cosonant. 
# Note: Characters can be upper or lowercase letters.


# letter = input("enter a char")
letter = 'E'

if letter in ['a','e','i','o','u','A','E','I','O','U']:
    result  = "vowel"
else: result  = "cosonant"

print(result)