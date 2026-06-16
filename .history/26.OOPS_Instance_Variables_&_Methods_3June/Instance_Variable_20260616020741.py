# """
# Instance Variable is a variable defined inside the __init__() method using self.

# Its value is unique for each object — every object has its own separate copy in memory (RAM).
# """
# print("start program")
class Employee:
    def __init__(self, emp_name, department):
        self.emp_name   = emp_name    # instance variable
        self.department = department  # instance variable

emp1 = Employee('Alex',   'Engineering')
emp2 = Employee('Jordan', 'Marketing')

# In RAM: TWO separate emp_name values!
print(emp1.emp_name)   # Alex
print(emp2.emp_name)   # Jordan  ← independent!