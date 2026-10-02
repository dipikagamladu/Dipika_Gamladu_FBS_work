#Write a Python program to remove the intersection of a second set with a first set.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}

result = set1 - set2

print("First set:", set1)
print("Second set:", set2)
print("After removing intersection:", result)