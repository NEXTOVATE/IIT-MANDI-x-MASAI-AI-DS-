# Q9 (4 Marks): Write Python code to deeply merge two dictionaries:
# d1 = {"a": {"x": 1}, "b": 2}
# d2 = {"a": {"y": 3}, "c": 4}
# Expected Output: {"a": {"x": 1, "y": 3}, "b": 2, "c": 4}
def deep_merge(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged         

n = deep_merge(dict1 = {"a": {"x": 1}, "b": 2}, dict2 = {"a": {"y": 3}, "c": 4})
print(n)