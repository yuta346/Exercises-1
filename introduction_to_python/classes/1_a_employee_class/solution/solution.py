#Completed

# ## Problem Description
# Define a Python class Employee with the following attributes:
# * `name` - a string
# * `employee_id` - an integer
# * `salaray` - an integer between 20,000 - 200,000
# * `years_at_company` - an integer
# Create an employee object with name `Cosette Rodger`, having an employee ID of `1`, a salary of `100000`, 
# and having been at the company for `4` years. Assign the person object to the variable name `cosette`.


class Employee:
    def __init__(self,name,employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

cosette = Employee('Cosette Rodger',1,100000,4)
