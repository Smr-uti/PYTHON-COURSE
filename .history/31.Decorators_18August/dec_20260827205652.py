def decor(detail):
    def inner():
        return detail().upper()

def decor2():
    def inner():
        return deta





def get_name():
    name = input("Enter your first name: ")
    sir_name = input("Enter your last name: ")
    full_name =name + sir_name
    return full_name