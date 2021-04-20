#Completed
# Code your solution here
## Problem Description
# Write a Python script that declares a variable `x` which is set to a value of 50.
# Construct a loop that goes from `0` to `x` inclusive, and stores all the values 
# which are divisible by 5 and 7 in a variable called `data`. 

x = 50
data = []
for i in range(50+1):
    if i%5==0 or i%7==0:
        data.append(i)

print(data)