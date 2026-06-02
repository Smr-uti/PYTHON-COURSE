import json

with open("data.json","w+") as fobj:
    result=json.load(fobj)

print(result)py