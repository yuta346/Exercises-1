#test case doesnt run

# Code your solution here
from provided_code import set1, set2

## Motivation
# Sets in python are same as sets in mathematics. 

# + '|' set union
# + '-'  set difference 
# + '<=' set subset 
# + '&' set intersection

# ## Problem Description
# Given a two sets, `set1` and `set2` that are hidden from you. Do not peak! Write a python script that 
# finds the differences between the two sets and stores these values in a variable called `diff`.


diff = set1 - set2

set1 = {'apple','orange','kiwi'}
set2 = {'apple','orange','grape'}
diff = set1 - set2
print(diff)