from threading import Thread

def display():
    msg="Jay shree ganesh!"
    return msg

t1=Thread(target=displa)
response=display()
print(response)

