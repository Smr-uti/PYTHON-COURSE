import json

with open("data.json", "r") as fobj:
    
    content = fobj.read()
    
    # स्ट्रिंगचे ऑब्जेक्टमध्ये रूपांतर केले
    data = json.loads(content)

print(data)