
from threading import Thread
import threading
def display1():
    for i in range(1,10):
        print("jai shree ganesh!")

def display2():
    for i in range(1,10):
            print("jai shree ganesh!!!!!!!")

t1=Thread(target=display2)
t2=Thread(target=display1)
t1.start()
t2.start()
# print(t1.name)
# print(t2.name)

# print(t1.ident)
# print(t2.ident)

current_thread=threading.current_thread()

# print(current_thread.name)
# print(current_thread.ident)