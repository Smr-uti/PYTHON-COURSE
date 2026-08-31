def my_range(start, end):
    for i in range(start, end):
        yield i

gen=my_range(5, 16)       
for i in gen:
    pri