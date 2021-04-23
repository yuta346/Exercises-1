#need to revisit

# ## Problem Description
# Define a recursive Python function named `count_down_from` that consumes one argument `num`. 
# The function prints the numbers from `1` to `num` (inclusive) in descending order, one on each line. 
# Do not use iteration of any form for this question.

# ## Example
# ```
# count_down_from(5)
# prints
# 5
# 4
# 3
# 2
# 1
# ```

def count_down_from(num):
    if num==0:
        return 
    print(num)
    return count_down_from(num-1)
count_down_from(10)