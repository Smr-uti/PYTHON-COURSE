def decor(func):
    def inner():
        return func().upper()

def decor2(func):
    def inner():
        return func().split()
    return inner

def get_name():
    name=input("Enter the first name")
    sir_name=input("Enter the sir name")
    full_name=name+sir_name
    return full_name

get_nme=decor1