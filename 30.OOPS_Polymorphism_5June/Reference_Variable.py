
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)

user=Employee("Akshay",20000)
user.display()
# print(user.salary)
# print(user.name)
user2=user
print(id(user))
print(id(user2))
user2.display()
print(user2.salary)
print(user2.name)
user3=user
user4=user
user5=user
user6=user
print("===============")
user6.display()
user6.name="ganesh"
print("===============")
user.display()
