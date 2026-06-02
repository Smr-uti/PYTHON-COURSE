print("Start Program")

class Vehicle:
    def __init__(self):
        self.colour=colo
        self.top_speed=200
        self.mileage=22

    def display_info(self):
        print("Mileage:", self.mileage)
        print("Top Speed:", self.top_speed)

obj1 = Vehicle()
print(obj1.colour)
print(obj1.top_speed)
print(obj1.mileage) 
obj1.display_info()

print("End Program")