import json

with open("data.json", "r") as fobj:
    
    content = fobj.read()
    
   




   
    data = json.loads(content)

print(data)