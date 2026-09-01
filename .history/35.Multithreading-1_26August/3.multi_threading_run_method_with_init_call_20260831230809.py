
from threading import Thread
class MyClass(Thread):
    def __init__(self,voting):
        super().__init__()
        print("constructor called")
        self.voting=voting
    def run(self):
        if self.voting:
            print("you are eligible for voting")

t1=MyClass(True)

t1.start()