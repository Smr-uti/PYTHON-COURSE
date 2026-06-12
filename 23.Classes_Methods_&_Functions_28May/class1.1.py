# print("Start program")

class BankATM:
    def __init__(self):
        print("ID of self is:", id(self))
        print("Constructor has been automatically called when you created an object")

    def Method1(self):
        print("This is normal method & you have to explicitly call it")

obj1 = BankATM()
obj1.Method1()

print("ID of obj1 is:", id(obj1))


# print("End program")