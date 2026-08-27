def decor1(func):
    def inner():
        return func().upper()
    return inner

def decor2(func):
    def inner():
        return func.split()
    return inner

@
def get_name():
    first_name=input("Enter your first name: ")
    sir_name=input("Enter your sirname: ")
    get_name= name + " " + sir_name

print(get_name)