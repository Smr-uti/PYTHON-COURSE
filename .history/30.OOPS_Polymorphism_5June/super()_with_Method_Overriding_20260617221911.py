print("start program")
class Vehicle:
    def start(self):
        print('Checking fuel/battery...')
        print('Ignition system initialized')

class ElectricCar(Vehicle):
    def start(self):
        super().start()              # Parent's code first
        print('Electric motor powered on!')
        print('Navigation system ready')

car = ElectricCar()
car.start()