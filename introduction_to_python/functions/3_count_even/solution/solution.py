#Completed

# ## Problem Description
# Write a python function `count_even` with a variable-length argument `*args` of integers. 
# Return the number of even integers are in `*args`.

# ## Example
# ```
# count_even(1, 2, 3, 4) == 2

def count_even(*args):
    count = 0
    for arg in args:
        if arg%2==0:
            count+=1
    return count

print(count_even(2, 4, 6, 8, 10))