class Vehicle:
    def start(self):
        print('Vehicle starting...')
    def describe(self):
        print('I am a generic vehicle')

class ElectricCar(Vehicle):
    def start(self):                    # OVERRIDES Vehicle.start()
        print('Electric car starting silently...')
    def describe(self):                 # OVERRIDES Vehicle.describe()
        print('I am an electric vehicle — zero emissions!')

car = ElectricCar()
car.start()     # Child's version runs!
car.describe()  # Child's version runs!