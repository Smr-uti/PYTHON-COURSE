
import time
from threading import Thread,RLock

Rlock_obj=RLock()

def display(message):
    Rlock_obj.acquire()
    Rlock_obj.acquire()
    for i in range(5):
        print(message)
        time.sleep(1)
    Rlock_obj.release()
    Rlock_obj.release()

t1=Thread(target=display,args=("jai ganesh",))
t2=Thread(target=display,args=("Jai shree ganesh",))

t1.start()
t2.start()