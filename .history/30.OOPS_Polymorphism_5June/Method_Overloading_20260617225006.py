print("Start program")
class Calculator:
    def add(self, x, y, z=0, w=0):   # 2, 3 या 4 numbers!
        return x + y + z + w

    def greet(self, name, greeting='Hello'):  # default greeting
        return f'{greeting}, {name}!'

calc = Calculator()
print(calc.add(5, 10))            # 15  (z=0, w=0 defaults)
print(calc.add(5, 10, 15))        # 30  (w=0 default)
print(calc.add(5, 10, 15, 20))    # 50  (all 4 provided)
print(calc.greet('Arjun'))            # Hello, Arjun!
print(calc.greet('Arjun', 'Namaste')) # Namaste, Arjun!