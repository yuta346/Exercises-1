#completed

# ## Problem Description
# Write a Python function `concat_args` that takes a variable length arguement `*args` 
# which contains string objects and returns the concatination the variables. If `*args` is empty output the empty string.

# ## Example
# ```
# concat_args("Hello ", "There") == "Hello There"
# ```

def concat_args(*args):
    result = ''
    if not args: return ''
    for arg in args:
        result+=arg
    return result
print(concat_args("Hello ", "World"))