import time
import threading
from threading import Thread
def display():
    time.sleep(1)
    print("jai ganesh")
    print("thread_id:",threading.get_ident())

t1=Thread(target=display)
t1.start()
print(t1.ident)
print("main_thread:",threading.get_ident())

import threading

print("jai ganesh")

current_thread=threading.current_thread()

print(current_thread.name)
print("main_thread:",current_thread.ident)