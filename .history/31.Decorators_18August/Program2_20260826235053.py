def decor(func):
    def inner():
        func()
        print()
    return inner