from threading import Thread

class MyClass(Thread):
    super().__init__()
    print("Construc")

t1=MyClass()
t1.start()
