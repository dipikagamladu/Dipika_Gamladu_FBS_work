#Write a program to create a duplicate of an existing list.
#  It should not point to same list.
list = [10, 20, 30, 40]
duplicate = []

for i in list:
    duplicate = duplicate + [i]

print("Original list =", list)
print("Duplicate list =", duplicate)

duplicate = duplicate + [50]

print("After changing duplicate list:")
print("Original list =", list)
print("Duplicate list =", duplicate)