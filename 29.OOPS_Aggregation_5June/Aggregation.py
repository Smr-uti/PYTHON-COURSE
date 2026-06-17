print("start program")
class Address:
    def __init__(self, city, pin, state):
        self.city  = city
        self.pin   = pin
        self.state = state

    def get_city(self):         # getter method
        return self.city

    def edit_address(self, new_city, new_pin, new_state):
        self.city  = new_city
        self.pin   = new_pin
        self.state = new_state

class Customer:
    def __init__(self, name, gender, address):
        self.name    = name
        self.gender  = gender
        self.address = address    # HAS-A: Address object stored!

    def print_address(self):
        print(self.address.city, self.address.pin, self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)

# ── Usage ──────────────────────────────────────────
addr = Address('pune', 412105, 'maharashtra')
cust = Customer('ganesh', 'male', addr)   # pass Address object
cust.print_address()                       # pune 412105 maharashtra
cust.edit_profile('ankit','mumbai',111111,'maharastra')
cust.print_address()                       # mumbai 111111 maharastra