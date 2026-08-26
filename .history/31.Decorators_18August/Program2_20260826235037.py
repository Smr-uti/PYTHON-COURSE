def decor(func):
    def inner():
        func()
    return inn