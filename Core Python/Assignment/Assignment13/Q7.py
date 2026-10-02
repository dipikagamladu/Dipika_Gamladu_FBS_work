#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. 
# Use the Python set.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing numbers in second set:", missing_in_set2)
print("Missing numbers in first set:", missing_in_set1)