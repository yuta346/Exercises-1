#Completed

from provided_code import d
# Code your solution here
## Problem Description
# In the solution.py file, you will be provided with a dictionary called `d` 
# which is hidden from you. Do not peek in the provided_code.py file! 
# The keys in this dictionary will be integers in the range from 1-5 inclusive, except one number in the range will be missing. 
# The values will be strings. Your goal is to use conditional statements to find the missing number in that range and 
# add a new key-value pair to `d` with the missing key, and string value `"found it!"`.



for i in range(1,6):
    if d.get(i, 'Not Found') == 'Not Found':
        d[i]='found it!'



# _dict = {1 : 'IN', 2 : 'AU', 3 : 'BR',4 : 'JP', 6 : 'MA'}
# for i in range(1,6):
#     if _dict.get(i, 'Not Found') == 'Not Found':
#         _dict[i]='found it!'
    
# print(_dict)
