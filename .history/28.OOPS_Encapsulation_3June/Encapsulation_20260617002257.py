print("start program")
class BankMachine:
    def __init__(self):
        self.secret_pin = ""  # instance variable
        self.__account_balance=1000 # instance variable
        print("constructor has been called")
    def withdraw(self,amt):   # instance method
        if self.account_balance >= amt:
            self.account_balance= self.account_balance - amt
    def retrieve_balance(self):
        return self.__account_balance
    def modify_balance(self,new_balance):
        if type(new_balance)==int:
            self.__account_balance=new_balance
        else:
            print("invalid balance!")

m1=BankMachine()
#print(m1.__account_balance)
print(m1.retrieve_balance())

m1.modify_balance(5000)
print(m1.retrieve_balance())
# m1.withdraw(500)
# print(m1.account_balance)
