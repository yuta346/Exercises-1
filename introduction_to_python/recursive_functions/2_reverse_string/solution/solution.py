#Completed

# ## Problem Description
# Define a recursive Python function named `reverse` that consumes one argument `string`. 
# The function returns the a string whos contents is the reverse of `string` 
# Do not use iteration of any form for this question.

# ## Example
# ```
# reverse("hello") == "olleh"
# ```

# def reverse(string):
#     if not string:
#         return string
#     return string[-1]+reverse(string[:-1])
# print(reverse("hellooooo"))


def reverse(string):
    return "" if string == "" else reverse(string[1:]) + string[0]
print(reverse("hellooooo"))