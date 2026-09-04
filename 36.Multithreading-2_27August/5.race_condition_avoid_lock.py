import threading
from threading import Thread, Lock

lock_obj=Lock()
class Bus:
    def __init__(self,name,available_seats):
        self.name=name
        self.available_seats=available_seats

    def reserve(self,needed_seats):
        current=threading.current_thread().name
        lock_obj.acquire()
        if self.available_seats>=needed_seats:
            print(f"{needed_seats} seat has been allocated to {current}")
            self.available_seats=self.available_seats-needed_seats
        else:
            print(f"sorry seats are not available for {current}")
        lock_obj.release()

bus1=Bus("Ganesh Travels",1)

t1=Thread(target=bus1.reserve,args=(1,),name="ganesh")
t2=Thread(target=bus1.reserve,args=(1,),name="mahesh")

t1.start()
t2.start()