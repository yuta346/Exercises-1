# Code your solution here
## Problem Description
# Write a Python script in *solution.py* that asks the user for 3 numbers as input. 
# Store these numbers in the variable names `num1`, `num2` and `num3` respectively.
# Create a variable called `avg` which stores the average of `num1`, `num2` and `num3`.

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
avg  = sum([num1,num2,num3])/3
print(avg)