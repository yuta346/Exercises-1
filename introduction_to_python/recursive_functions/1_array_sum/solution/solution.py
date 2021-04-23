#Completed

# ## Problem Description
# Define a recursive Python function named `sum_array` that consumes one parameter `num_list` 
# and returns the sum of the the numbers within the list. Do not use iteration or 
# any built-in functions of any form for this question.

# ## Example
# ```
# sum_array([1, 2, 3, 4]) == 10
# ```

def sum_array(num_list):
    print(num_list)
    if len(num_list)==0:
        return 0
    return num_list[0]+sum_array(num_list[1:])
print(sum_array([1, -2, 3.5]))