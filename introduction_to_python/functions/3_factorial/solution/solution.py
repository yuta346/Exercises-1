#Completed -- recursive method did not work

# ## Problem Description
# Write a Python function `factorial` that consumes a non-negative integer `n`, and returns the factorial of `n`.

# **DO NOT USE factorial() built in method**

# ## Example
# ```
# factorial(3) == 6
# ```

#recursive
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial(n-1)
# print(factorial(3))

#iterative
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

print(factorial(1))