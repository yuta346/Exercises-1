# Define variables a, b, c, d
## Problem Description 
# In the **solution.py** file, define variables `a`, `b`, `c`, and `d` such that 
# the following Python expressions all evaluate to `True`.

# `type(a) == list`
# `type(c) == float`
# `type(a or b) == str`
# `(d and b) == "rocketship"`
# `(b or d) == "rocketship"`
# `(c and d) == 0.0`
# `type(c or d) == int`
# `c + d == 5.0`

a = []
b = "rocketship"
c = 0.0
d = 5

print(d and b)

print(type(a) == list)
print(type(c) == float)
print(type(a or b) == str)
print((d and b) == "rocketship")
print((b or d) == "rocketship")
print((c and d) == 0.0) #c(0.0)==false
print(type(c or d) == int)
print(c + d == 5.0)