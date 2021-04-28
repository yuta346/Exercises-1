#Completed

# # Problem Description
# Define a function `give_raises` that consumes `employee_lst`, a list of employee objects 
# as defined in the previous question, and mutates each employee object in the list such that each employee 
# is given a raise to their salary according to the following criteria:
# * An employee gets a raise of $5,000 if they have been at the company for <= 5 years.
# * An employee gets a raise of $8,000 if they have been at the company for > 5 and < 10 years.
# * An employee gets a raise of $10,000 if they have been at the company for >= 10 years.

# ## Example
# ```
# emp1 = Employee("John", 1, 45000, 8)
# emp2 = Employee("Jane", 2, 22000, 1)
# emp3 = Employee("Marie", 3, 90000, 10)

# give_raises([emp1, emp2, emp3]) == None
# emp1.salary == 53000
# emp2.salary == 27000
# emp3.salary == 100000

# ```

class Employee:
    def __init__(self,name,employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

    def give_raises(self, employee_lst):
        for emp in employee_lst:
            emp.give_raise()

    def give_raise(self):
        if self.years_at_company >=10 :
            self.salary+=10000
        elif self.years_at_company<10 and self.years_at_company>5:
            self.salary+=8000
        else:
            self.salary+=5000
                



