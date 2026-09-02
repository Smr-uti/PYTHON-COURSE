from threading import Thread
import time

def display1():
    time.sleep(1)
    print("Jai Ganesh")

def display2():
    time.sleep(1)
    print("Jai Ganesh") 

t1=Thread(target=display1)
t2=Thread(target=display2)
start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print("Total time taken: ", end-start)