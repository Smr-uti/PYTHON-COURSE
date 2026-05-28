import json

with open("data.json", "r") as fobj:
    # फाईलमधून डेटा स्ट्रिंगमध्ये वाचला
    content = fobj.read()
    
    # स्ट्रिंगचे ऑब्जेक्टमध्ये रूपांतर केले
    data = json.loads(content)

print(data)