print("start program")
class BankMachine:
    cust_counter = 1   # Static variable

    def __init__(self):
        self.cust_id = BankMachine.cust_counter
        BankMachine.cust_counter += 1
    
    def display(self):
        print("customer id is",self.cust_id)

    @staticmethod
    def get_total_customers():    # no self!
        return BankMachine.cust_counter - 1

    @staticmethod
    def validate_pin_format(pin_str):  # utility function
        return pin_str.isdigit() and len(pin_str) == 4

m1 = BankMachine()
m2 = BankMachine()

# Call via class name (recommended!)
print(BankMachine.get_total_customers())   # 2
print(BankMachine.validate_pin_format('4523'))  # True
print(BankMachine.validate_pin_format('ab12'))  # False
m1.display()