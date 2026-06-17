print("start program")
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):                    # print(f1) → '1/2'
        return f'{self.num}/{self.den}'

    def __add__(self, other):  # f1 + f2
        # a/b + c/d = (a*d + b*c) / (b*d)
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __sub__(self, other):  # f1 - f2
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)

    def __mul__(self, other):  # f1 * f2
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):  # f1 / f2 (flip!)
        return Fraction(self.num * other.den, self.den * other.num)

f1 = Fraction(3, 4)  # 3/4
f2 = Fraction(1, 2)  # 1/2
print(f1 + f2)  # 10/8
print(f1 - f2)  # 2/8
print(f1 * f2)  # 3/8
print(f1 / f2)  # 6/4