from threading import Thread
import threading
def display():
    msg="Jay shree ganesh!"
    print(msg)

def display2():
    msg="Jay shree ganesh!!!!"
    print(msg)

t1=Thread(target=display2)
t2=Thread(target=display)

t1.start()
t2.start()

print(t1.name)
print(t2.name)

print(t1.ident)
print(t2.ident)

current_thread=threading.current_thread()

p