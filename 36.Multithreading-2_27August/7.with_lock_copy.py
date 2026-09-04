
import time
from threading import Thread,Lock

lock_obj=Lock()

def display(message):
    lock_obj.acquire()
    for i in range(5):
        print(message)
        time.sleep(1)
    lock_obj.release()

t1=Thread(target=display,args=("jai ganesh",))
t2=Thread(target=display,args=("Jai shree ganesh",))

t1.start()
t2.start()