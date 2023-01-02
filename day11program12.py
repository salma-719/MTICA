sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"}
keys = ["name", "salary"]

res = dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
