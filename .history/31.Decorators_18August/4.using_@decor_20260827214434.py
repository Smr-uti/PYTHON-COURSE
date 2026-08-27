def decor1(func):
    def inner():
        return func().upper()
    return inner

def decor2(func):
    def inner():
        return func().split()
    return inner

@decor2
@decor1
def get_name():
    first_name=input("Enter your first name: ")
    sir_name=input("Enter your sirname: ")
    full_name= first_name + " " + sir_name
    return full_name

print(get_name())