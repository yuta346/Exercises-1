#Completed

# ## Problem Description
# Define a recursive Python function named `power` that consumes two parameters `a` and `b`. 
# The function returns `a` to the power of `b`. Do not use the `**` operator or iteration in this question.

# ## Example
# ```
# power(2, 3) == 8
# ```

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a, b-1)
print(power(2,3))