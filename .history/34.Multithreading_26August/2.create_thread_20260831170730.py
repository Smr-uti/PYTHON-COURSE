from threading import Thread

def display():
    msg="Jay shree ganesh!"
    return msg

t1=Thread(target=display)
t1.start

