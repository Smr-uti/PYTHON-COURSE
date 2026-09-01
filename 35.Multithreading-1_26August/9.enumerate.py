from threading import Thread
import threading

def display():
    print("Jay ganesh")

t1=Thread(target=display)
t1.start()

print(t1.is_alive())

print(threading.enumerate())