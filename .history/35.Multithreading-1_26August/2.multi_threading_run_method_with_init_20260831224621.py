from threading import Thread

class MyClass(Thread):
    super().__init__()
    print("Jay Ganesh")

t1=MyClass()
t1.start()
