#Completed. test case might have a bug

# Code your solution here
## Problem Description
# Write a Python script that asks the user for a string value stored in object `string`.
# Your goal is to check whether the value is in upperCase, and if so convert the data into lowerCase. 
# Otherwise, if value is in lowerCase, convert the data into upperCase and store the result in a new variable called `data`. 

# string = input("enter string:")
string = "UNIVERSE"

if string.isupper(): data = string.lower()
else: data  = string.upper()
print(data)
