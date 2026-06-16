class Student:
    def __init__(self, name, grade):
        self.name = name    # Instance Variable
        self.grade = grade  # Instance Variable

    # This is an Instance Method
    def display_info(self):
        return f"Student: {self.name}, Grade: {self.grade}"

# Creating an object (Instance)
s1 = Student("Amit", "A")

# Calling the instance method
print(s1.display_info())