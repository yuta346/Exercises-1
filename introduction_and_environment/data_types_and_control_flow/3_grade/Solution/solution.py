# Code your solution here
from provided_code import grades

## Motivation
#Completed

# Student Grade determines the next step to success. 

# + 90-100 -> A 
# + 70-89-> B 
# + 50-69-> C
# + 35-49-> D 
# + Less than 35-> F

# ## Problem Description
# Given a list of grades `grades` that is hidden from you. Do not peak! Write a Python script that defines a list called 
# `letter_grades` that contains the corresponding student letter grade for each grade in `grades`. 

# grades = [90, 90, 69, 50, 35, 10]
letter_grades = []
for grade in grades:
    if grade >=90:
        letter_grades.append('A')
    elif grade >=70:
        letter_grades.append('B')
    elif grade >=50:
        letter_grades.append('C')
    elif grade >=35:
        letter_grades.append('D')
    else: letter_grades.append('F')
print(letter_grades)
