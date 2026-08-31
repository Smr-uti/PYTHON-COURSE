
from threading import Thread
class MyClass(Thread):
    def __init__(self,voting):
        super().__init__()
        print("constructor called")
        self.voting=voting
    def run(self):
        if self.voting:
            print("you are eligible for voting")
        self.demo()
    
    def demo(self):
        print("this is the demo method")

t1=MyClass(True)

t1.start()