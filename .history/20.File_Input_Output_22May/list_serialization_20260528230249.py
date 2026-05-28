import json

nums = [10, 20, 30, 40, 50]
with open("n.json", "w") as f:
    json.dump(nums, f)