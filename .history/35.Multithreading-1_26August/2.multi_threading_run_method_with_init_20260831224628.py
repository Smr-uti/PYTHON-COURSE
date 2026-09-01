from threading import Thread

class MyClass(Thread):
    super().__init__()
    print("")

t1=MyClass()
t1.start()
