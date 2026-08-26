def decor(func):
    def inner():
        func()
        print("We")
    return inner