#test case has some bug

# Code your solution here
## Problem Description
# Write a Python script that asks the user for two inputs, a string value and an integer value, 
# representing the number of times the user wishes to duplicate the string.
# Store the input values as `str1` and `mult ` respectively. Then, in a new variable called `result` 
# store a string which is `str1` repeated `mult` number of times.

str1 = input("Enter string:")
mult = int(input("Enter integer value you want to duplicate string:"))
result  = str1*mult

str1 = "hi"
mult = 3
result  = str1*mult
print(result)
