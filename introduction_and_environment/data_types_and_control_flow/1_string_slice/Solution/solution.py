#Completed

# Code your solution here
## Problem Description
# Write a python script that contains a variable called `string` with the value `"Hello Universe"`.
# Using string indexing extract the substring `"Hello"` from `string` and store the result in a variable called `substr`.
# Concatenate `substr` with the string `" World"` and store result in a variable called `salutation`.

string = "Hello Universe"

substr = string[:5]
salutation = substr+" World"
print(salutation)