#Completed

# ## Problem Description
# Write a Python function `sum_data` that consumes a list of integers `lst` 
# and returns the sum of all the integers in `lst`. Try doing this exercise without using the built in sum() function.

#  ***DO NOT USE THE BUILT-IN SUM()***

# ## Example
# ```
# sum_data([2, 4, 6, 8]) == 20
# ```

def sum_data(lst):
    Sum = 0
    for i in lst:
        Sum+=i
    return Sum
