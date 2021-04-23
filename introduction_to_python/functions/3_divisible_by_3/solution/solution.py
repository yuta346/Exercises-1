#Completed

# Write your code here
## Problem Description
# Write a python function `divisible_by_3` with a variable-length arguement `*args` of integers, 
# and returns a list of all the numbers in `*args` divisible by three.

# ## Example
# ```
# div_by_3(2, 3, 5, 6, 9) == [3, 6, 9]
# ```

def divisible_by_3(*args):
    result  = []
    for arg in args:
        if arg%3==0:
            result.append(arg)
    return result
