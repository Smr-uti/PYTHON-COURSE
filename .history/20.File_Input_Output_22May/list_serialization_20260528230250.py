import json

nums = [10, 20, 30, 40, 50]
with open("da.json", "w") as f:
    json.dump(nums, f)