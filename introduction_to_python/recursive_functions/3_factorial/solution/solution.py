#Completed

# ## Problem Description
# Define a recursive Python function named `factorial_recursive` that consumes 
# a number `n` and returns the factorial `n!` of `n`.

# ## Example
# ```
# factorial_recursive(4) == 24
# ```

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(4))