from functools import reduce

class Student:

    def __init__(self,name,age,grades):

        self.name = name
        self.age = age
        self.grades = grades


def highest_avg(stud_lst):
    max_average = 0
    max_avg_student_name =''
    for student in stud_lst:
        if student.grades:
            average_score = reduce(lambda x,y: x+y, student.grades)/len(student.grades)
        else: 
            average_score = 0
        if average_score > max_average:
            max_average = average_score
            max_avg_student_name = student.name
        elif average_score == max_average:
            max_avg_student_name = min(student.name, max_avg_student_name)
    return max_avg_student_name
        
            
Anton = Student("Anton", 29, [100, 50]) #403/5 = 80.6
Nell = Student("Nell", 26, [100, 90]) #94
Cosette = Student("Cosette", 20, [100,50]) #88.8
print(highest_avg([Anton, Nell, Cosette]))        



# Anton = Student("Anton", 29, [75, 82, 96, 100, 50]) #403/5 = 80.6
# Nell = Student("Nell", 26, [98, 95, 89, 92, 100, 90]) #94
# Cosette = Student("Cosette", 20, [85, 72, 96, 99, 92]) #88.8
# print(highest_avg([Anton, Nell, Cosette])) 