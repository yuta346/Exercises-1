#Completed

# ## Problem Description
# Define a two mutually recursive Python function named `hofstaderA` and `hofstaderB` 
# that both consume a non-negative integer `n`. `hofstaderF` will return `A(n)` 
# and `hofstaderB` will return `B(n)` where `A(n)` and `B(n)` are defined as follows:
# ```
# A(0) = 1
# A(n) = n - B(A(n-1)), n > 0
# B(0) = 0
# B(n) = n - A(B(n-1)), n > 0
# ```
# ## Example
# ```
# hofstaderA(4) == 3
# hofstaderB(6) == 4
# ```

def hofstaderA(n):
    if n==0:
        return 1
    return n - hofstaderB(hofstaderA(n-1))
def hofstaderB(n):
    if n==0:
        return 0
    return n - hofstaderA(hofstaderB(n-1))

print(hofstaderA(4))
print(hofstaderB(6))