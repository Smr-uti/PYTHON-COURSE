
from threading import Thread

class Demo:
    @staticmethod
    def display():
        print("Jay Shri Ganesh!")

t1=Thread(target=Demo.display)
t1.start()