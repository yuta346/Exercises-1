#Completed but test case has bug..

# Write your solution here
## Problem Description
# Write a Python function `below_100` that consumes an integer `n`.
# If `n` is less than equal to 100 return `"less than 100"`, otherwise return `"greater than 100"`.

# ## Example
# ```
# below_100(200) == "greater than 100"
# below_100(50) == "less than 100"

def below_100(n):
    if n <100: 
        return "less than 100"
    else:return 'greater than 100'

