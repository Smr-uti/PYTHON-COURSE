print("Sclass Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    #getter
    def show(self):
        print (self.price)
        print(self.brand) 
        print(self.camera )

class SmartPhone(Phone):
    # def __init__(self, price1, brand1, camera1):
    #     print ("Inside phone constructor")
    #     self.price1 = price1
    #     self.brand1 = brand1
    #     self.camera1 = camera1
    pass

s=SmartPhone(20000, "Apple", 13)
s.show()
