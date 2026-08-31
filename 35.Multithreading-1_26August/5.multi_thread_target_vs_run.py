
# from threading import Thread

# def add(a,b):
#     return a+b

# t1=Thread(target=add,args=(10,20))
# t1.start()


# #---------------------------------------

from threading import Thread
import time

class MyClass(Thread):
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b
        self.result=None
    def run(self):
        self.result=self.a+self.b

t1=MyClass(10,20)
t1.start()

print(t1.result)