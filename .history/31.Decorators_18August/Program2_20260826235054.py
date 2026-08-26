def decor(func):
    def inner():
        func()
        print("W")
    return inner