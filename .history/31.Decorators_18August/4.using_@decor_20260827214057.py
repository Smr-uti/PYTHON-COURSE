def decor1(func):
    def inner():
        return func().upper()
    return inner

def decor2(func):
    def inner():
        return func().split()
    return inner

@decor1
def get_name():
    first_name=input("Enter your first name: ")
    sir_name=input("Enter your sirname: ")
    full= first_name + " " + sir_name
    return full

print(get_name())