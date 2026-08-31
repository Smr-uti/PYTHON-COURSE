
from threading import Thread

class Demo:
    def display(self):
        print("jai shree ganesh!")


obj1=Demo()

t1=Thread(target=obj1.display)

t1.start()

print(t1.name)
print(t1.ident)