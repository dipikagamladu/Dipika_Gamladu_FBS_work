#5. Python Program to Sum All the Items in a Dictionary
dictionary = {1: 10, 2: 20, 3: 30, 4: 40,5:50}

total = 0

for i in dictionary.values():
    total = total + i

print("Sum of all items:", total)