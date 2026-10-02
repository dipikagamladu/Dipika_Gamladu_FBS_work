#WAP to print list after removing even numbers.
list = [10, 15, 20, 25, 30, 35]
new_list = []
for i in list:
    if i % 2 != 0:
        new_list = new_list + [i]

print("Original list =", list)
print("List after removing even numbers =", new_list)