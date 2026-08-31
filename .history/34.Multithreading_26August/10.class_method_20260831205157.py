from threading import Thread

class Demo:
    @classmethod
    def display(cls):
        print("Jay Ganesh")

t1=Thread(target=Demo.display)        
t1.start