#6. Python Program to Multiply All the Items in a Dictionary.
dictionary = {1: 2, 2: 3, 3: 4, 4:5}

result = 1

for i in dictionary.values():
    result = result * i

print("Multiplication of all items:", result)