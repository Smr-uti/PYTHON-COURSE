# 1. Base Class
class Person:
    def greet(self):
        print("Hello, I am a person.")

# 2. Intermediate Classes (Hierarchical)
class Student(Person):
    def study(self):
        print("I am studying.")

class Teacher(Person):
    def teach(self):
        print("I am teaching.")

# 3. Derived Class (Multiple Inheritance creating Hybrid)
class TeachingAssistant(Student, Teacher):
    def assist(self):
        print("I am assisting the professor.")

# Testing the Hybrid structure
ta = TeachingAssistant()
ta.greet()  # Inherited from Person
ta.study()  # Inherited from Student
ta.teach()  # Inherited from Teacher
ta.assist() # Defined in TeachingAssistant