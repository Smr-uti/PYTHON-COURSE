
from threading import Thread
# import threading
def display1():
    for i in range(1,5):
        print("jai shree ganesh!")

def display2():
    for i in range(1,5):
            print("jai shree ganesh!!!!!!!")

t1=Thread(target=display2)
t2=Thread(target=display1)
t1.start()
t2.start()
