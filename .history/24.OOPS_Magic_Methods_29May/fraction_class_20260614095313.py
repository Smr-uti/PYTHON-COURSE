print("Start Program")

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other):
        new_num = (self.numerator * other.denominator + other.numerator * self.denominator)         
        new_den = (self.denominator * other.denominator)
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = (self.numerator * other.denominator - other.numerator * self.denominator)
        new_den = (self.denominator * other.denominator)
        return Fraction(new_num, new_den)
    
    
fraction1 = Fraction(1, 2)
fraction2 = Fraction(7, 11)

print(fraction1)  # 1/2
print(fraction2)  # 7/11
print(fraction1 + fraction2) # 25/22
print
print("End Program")


