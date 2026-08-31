from threading import Thread

def display(msg, times):
    for i in range(times):
        print(msg)

t1=Thread(target=display, kwargs={
  "msg" = "Jay shri ga"  
})

t1.start()

