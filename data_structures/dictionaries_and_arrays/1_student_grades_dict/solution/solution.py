#Completed
from functools import reduce
def student_grades(sgrades,letter_grades):
    average_and_grades = tuple()
    average_grade = 0
    grade = ''
    new_dict = {name:None for name in list(sgrades.keys())}
    for key, val in sgrades.items():
        average_grade = int(reduce(lambda x,y:x+y,val)/len(val))
        if average_grade>90:
            grade = 'A'
            average_and_grades = (grade, average_grade)
            new_dict[key] = average_and_grades
        elif average_grade>75:
            grade = 'B'
            average_and_grades = (grade, average_grade)
            new_dict[key] = average_and_grades
        elif average_grade>60:
            grade = 'C'
            average_and_grades = (grade, average_grade)
            new_dict[key] = average_and_grades
        elif average_grade>45:
            grade = 'D'
            average_and_grades = (grade, average_grade)
            new_dict[key] = average_and_grades
        elif average_grade>30:
            grade = 'E'
            average_and_grades = (grade, average_grade)
            new_dict[key] = average_and_grades
        else: 
            grade = 'F'
            average_and_grades = (grade, average_grade)
            new_dict[key] = average_and_grades
    return new_dict
    


sgrades = {"Anton": [62, 55, 82], "Wasif": [100, 72, 94, 50], "Nell": [99, 100]}
letter_grades = {"A": (90, 100), "B": (75, 89), "C": (60, 74), "D": (45, 59), "E": (30, 44), "F": (1, 29)}
print(student_grades(sgrades, letter_grades))
#== {"Anton": ("C", 66), "Wasif": ("B", 79), "Nell": ("A", 99)}