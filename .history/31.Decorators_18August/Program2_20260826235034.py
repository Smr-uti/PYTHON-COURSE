def decor(func):
    def inner():
        func()
    ret