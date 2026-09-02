from threading import Thread
import time

def display1():
    time.sleep(1)
    print("Jai Ganesh")

def display2():
    time.sleep(1)
    print("Jai Ganesh") 

# 
start = time.time()

display1()
display2()

end = time.time()

print("Total time taken: ", end-start)