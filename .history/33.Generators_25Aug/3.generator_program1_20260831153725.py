def square(num):
    for i in range(1, num+1):
        yield i**2

gen=square        
print(next(gen))
print(next(gen))
print(next(gen))
print("========")
for i in gen:
    print(i)