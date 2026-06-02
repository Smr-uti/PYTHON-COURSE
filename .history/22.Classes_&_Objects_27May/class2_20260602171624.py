print("Start Program")

class Vehicle:
    def __init__(self, colour):
        self.colour=colour
        self.top_speed=top_speed
        self.mileage=mileage

    def display_info(self):
        print("Mileage:", self.mileage)
        print("Top Speed:", self.top_speed)

obj1 = Vehicle("Red", 200, 25)
print(obj1.colour)
print(obj1.top_speed)
print(obj1.mileage) 
obj1.display_info()

obj2 = Vehicle("White", 220, 30)
print(obj2.colour)
print(obj2.top_speed)
print(obj2.mileage)
obj2.display_info()

print("End Program")