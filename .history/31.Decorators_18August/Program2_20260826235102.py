def decor(func):
    def inner():
        func()
        print("Welcom")
    return inner

def