def calculate_sum(text):
    counter=0

    for char in text:
        counter=counter+1
    return counter

result=calculate_sum("pythonlearning.org")
print("length of string is:",result)