import time
import threading
from threading import Thread
def display():
    time.sleep(10)
    print("jai ganesh")

t1=Thread(target=display)
t2=Thread(target=display)
t3=Thread(target=display)

t1.start()
t2.start()
t3.start()

print(threading.active_count())

print(t1.is_alive())
print(t2.is_alive())
print(t3.is_alive())