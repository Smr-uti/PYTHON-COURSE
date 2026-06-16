# class BankMachine:
#     def __init__(self):
#         self.cust_id = 1  # Every starts at 1!

# m1 = BankMachine()  # cust_id = 1
# m2 = BankMachine()  # cust_id = 1  ???


#No shared counter exists!
print("start program")
class BankMachine:
    cust_counter = 1  # CLASS level! Shared # static variable
    def __init__(self):
        self.cust_id = BankMachine.cust_counter # instance variable
        BankMachine.cust_counter += 1

m1 = BankMachine()  # cust_id = 1

# m2 = BankMachine()  # cust_id = 2
# m3 = BankMachine()  # cust_id = 3

print(BankMachine.cust_counter)
