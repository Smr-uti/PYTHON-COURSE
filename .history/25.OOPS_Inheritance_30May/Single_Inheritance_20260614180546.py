# parent
class User:
  def __init__(self):
    self.name = 'ganesh'
    self.gender = 'male'

  def login(self):
    print('login')

# child
class Student(User):
  def __init__(self):
    self.rollno = 100

  def enroll(self):
    print('enroll into the course')

u = User()
s = Student()

#print(s.name)
s.login()
s.enroll()
print(s.rollno)
