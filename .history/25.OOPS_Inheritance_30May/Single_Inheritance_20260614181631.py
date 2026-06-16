class User:
    def __init__(self):
        self.name = "Ganesh"
        self.gender = "Male"

    def login(self):
        print("Login")


class Student(User):
    def __init__(self):
        sel