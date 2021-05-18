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

def fibonacci_dp(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    if n == 0:
        return dp[0]
    elif n == 1: 
        return dp[1]
    else:
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibonacci_dp(4))