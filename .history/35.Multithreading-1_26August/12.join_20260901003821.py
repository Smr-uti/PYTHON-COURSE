import time
from threading import Thread
def display():
    time.sleep(1)
    print("jai ganesh")
    print("this is the function run by thread1")

def display1():
    time.sleep(1)
    print("jai ganesh")
    print("this is the function run by thread2")

def demo():
    print("this is the function run by main thread")

t1=Thread(target=display)
t2=Thread(target=display1)
t1.start()
t2.start()
t1.join()
t2.join()
demo()