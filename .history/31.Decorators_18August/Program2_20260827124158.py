# def decor(func):
#     def inner():
#         func()
#         print("Welcome")
#     return inner

# def printer():
#     print("Welcome")
#     print("Welcome")

# inner=decor(printer)
# inner()


def decor(func):
    def inner():
        result = func()
        num3 = float(input("Enter third number"))
        result2= result + num3
        return e
    return inner
    
        
def addition():
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))

    result = num1 + num2
    return result

addition = decor(addition)
addition()