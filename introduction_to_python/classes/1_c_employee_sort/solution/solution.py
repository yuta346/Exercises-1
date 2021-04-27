#Completed

# # Problem Description
# Define a function `sort_employees` that consumes `employee_lst`, 
# a list of employee objects as defined in the previous question, 
# and returns a list of employee names sorted in alphabetical order.
# Hint: `from operator import attrgetter`

# ## Example
# ```
# emp1 = Employee("John", 1, 45,000, 8)
# emp2 = Employee("Jane", 2, 22,000, 1)
# emp3 = Employee("Marie", 3, 90,000, 10)

# sort_employees([emp1, emp2, emp3]) == ["Jane", "John", "Marie"]
# ```
from operator import attrgetter

class Employee:
    def __init__(self,name,employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

def sort_employees(employee_lst):
    employee_lst =  sorted(employee_lst,key=attrgetter('name'))
    return [emp.name for emp in employee_lst]


emp1 = Employee("John", 1, 45000, 8)
emp2 = Employee("Jane", 2, 22000, 1)
emp3 = Employee("Marie", 3, 90000, 10)
print(sort_employees([emp1, emp2, emp3]))