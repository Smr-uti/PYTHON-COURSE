from threading import Thread

def display():
    msg="Jay shree ganesh!"
    rmsg

t1=Thread(target=display)
t1.start()

print(t1.name)
print(t1.ident)

