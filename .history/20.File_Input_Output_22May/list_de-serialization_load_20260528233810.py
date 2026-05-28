import json

with open("data3.json","w+") as fobj:
    result=json.load(fobj)

print(result)