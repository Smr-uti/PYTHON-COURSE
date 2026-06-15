class Fraction:
    def __init__(self, x, y):
        self.numerator = x
        self.denominator = y

    def __str__(self):
        return '{}/{}'.format(self.numerator,self.denominator)

fraction1 = Fraction(1, 2)
fraction2 = Fraction(7, 11)     