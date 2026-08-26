def decor(func):
    def inner():
        func()
        print("Welc")
    return inner