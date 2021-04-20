#need to update the problem description


# Code your solution here
from provided_code import lst
## Problem Description
# In the solution.py file, you will be provided with a list called `lst` which is hidden from you.
#  Do not peek in the provided_code.py file! 
# Write a python script that creates a new list called `lst2` which contains all the item from 
# lst but adds a new item with the value `"new"` in the list at index 3.

lst = [1,2,3,4,5,6]
lst2 = lst
lst2.insert(3,'new')
print(lst2)


