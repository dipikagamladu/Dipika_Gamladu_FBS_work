#Write a Python program to find elements in a given set that are not in another set.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}

result = set1 - set2

print("Elements present in set1 but not in set2:", result)