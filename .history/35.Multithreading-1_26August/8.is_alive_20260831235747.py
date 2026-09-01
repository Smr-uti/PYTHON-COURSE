from threading import Thread

def display():
    print("Jay ganesh")

t1=Thread(target=display)
t1.start()

print(t1.)