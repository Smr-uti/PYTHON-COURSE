from threading import Thread

def display():
    msg="Jay shree ganesh!"
    print(msg)

def display2():
    msg="Jay shree ganesh!!!!"
    print(msg)

t1=Thread(target=display2)
t2=Thread(target=display)

t1.start()
t2.st
print(t1.name)
print(t1.ident)

