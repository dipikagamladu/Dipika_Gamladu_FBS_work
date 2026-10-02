#Python Program to Concatenate Two Dictionaries Into One
dict1 = {"name": "Dipika", "age": 22}
dict2 = {"city": "Pune", "course": "Python"}

dict1.update(dict2)

print(dict1)