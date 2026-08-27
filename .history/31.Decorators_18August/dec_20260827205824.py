def decor1(detail):
    def inner():
        return detail().upper()

def decor2(detail):
    def inner():
        return detail().split
    return inner

def get_name():
    name = input("Enter your first name: ")
    sir_name = input("Enter your last name: ")
    full_name =name + sir_name
    return full_name

get_name = decor1(get_name
                  )