import json

nums = [10, 20, 30, 40, 50]

# १. dumps वापरून लिस्टचे रूपांतर JSON स्ट्रिंगमध्ये केले
json_string = json.dumps(nums)

with open("data.json", "w") as fobj:
    fobj.write(json_string)