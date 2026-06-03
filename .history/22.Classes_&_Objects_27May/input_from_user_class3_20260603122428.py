print("Start Program")

class Vehicle:
    def __init__(self, colour, top_speed, mileage):
        self.colour = colour
        self.top_speed = top_speed
        self.mileage =mileage

    def display_info(self):
        print("Mileage:", self.mileage)
        print("Top Speed:", self.top_speed)

colour = input("Enter the colour of the vehicle: ")
top_speed = int(input("Enter the top speed of the vehicle: "))      
mileage = int(input("Enter the mileage of the vehicle: "))

obj1 = Vehicle(colour, top_speed, mileage)
print(obj1.colour)
print(obj1.top_speed)
print(obj1.mileage) 

obj1.display_info()

colour2 = input("Enter the colour of the second vehicle: ")
top_speed2 = int(input("Enter the top speed of the second vehicle: "))
mileage2 = int(input("Enter the mileage of the second vehicle: "))

obj2 = Vehicle(colour2, top_speed2, mileage2)
print(obj2.colour)
print(obj2.top_speed)
print(obj2.mileage)

obj2.display_info()

print("End Program")