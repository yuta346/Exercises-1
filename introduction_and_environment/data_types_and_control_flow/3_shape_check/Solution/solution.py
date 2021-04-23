# Code your solution here

## Motivation
#  3-Triangle , 4-Quadrilateral , 5-Pentagon , 6-Hexagon, 7-Heptagon, 8-Octagon, 9-Nonagon are just few shapes in geometry ranging 3-9.

## Problem Description
# Write a Python script that asks the user for an integer input stored in a variable called `g_int` in an infinate loop. 
# Create a list variable called `g_lst`, and for each valid geometric shape number the user enters in the range [3-9], 
# append the coresponding shape name string to `g_lst`. If the user enters an invalid geometric shape number outside the range [3-9], 
# break out of the loop. Note: The first letter of each shape name should be capitalized. 
# You may find it useful to create a dictionary mapping numbers as keys, to their corresponding shape string.

shape_dict = {3:'Triangle', 4:'Quadrilateral',5:'Pentagon',6:'Hexagon',7:'Heptagon',8:'Octagon',9:'Nonagon'}
g_lst = []

while True:
    g_int = int(input("enter an integer"))
    if shape_dict.get(g_int):
        g_lst.append(shape_dict[g_int])
    else:
        break
print(g_lst)