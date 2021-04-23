#Completed

# ## Problem Description
# Define a recursive Python function named `fibonacci` that consumes one argument `n`. 
# The function returns the `n`th fibonacci number or `-1` if `n <= 0`. To understand 
# what a fibonacci number is, please reference [wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number). 
# Do not use iteration for this question.

# ## Example
# ```
# fibonacci(4) == 3
# ```

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))