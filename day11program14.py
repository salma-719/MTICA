sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"}
keys = ["name", "salary"]

d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]

print(d)
