#Completed

# ## Problem Description
# Write a Python function `shut_down` that consumes a boolean value `x`.
# If `x` is the boolean value `True` return the string `"SHUTDOWN"`, otherwise return the string `"SHUTDOWN ABORTED"`.

# ## Example:
# ```
# shut_down(True) == "SHUTDOWN"
# ```

def shut_down(x):
    if x == True: return "SHUTDOWN"
    else: return "SHUTDOWN ABORTED"