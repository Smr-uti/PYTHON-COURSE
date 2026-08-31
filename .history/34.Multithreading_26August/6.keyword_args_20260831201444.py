from threading import Thread

def display(msg, times):
    for i in range(times):
        print(msg)

t1=Thread(target=display, kwargs=("jay ganesh.!!", 10))

t1.start()

