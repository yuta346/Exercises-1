# ## Problem Description
# Define a recursive Python function named `multiply` that consumes two parameters `a` and `b`. 
# The function returns `a` multiplied `b`. Do not use the `*` operator or iteration in this question.

# ## Example
# ```
# multiply(2, 3) == 6
# ```

def multiply(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

print(multiply(2,3))