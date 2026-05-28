import json

nums = [10, 20, 30, 40, 50]


json_string = json.dumps(nums)

with open("data.json", "w") as fobj:
    fobj.write(json_string)