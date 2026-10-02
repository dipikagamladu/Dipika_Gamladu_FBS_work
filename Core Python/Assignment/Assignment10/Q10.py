#WAP to remove all occurrence of a  given element in the list.
list = [10, 20, 10, 30, 10, 40]
number = int(input("Enter element to remove: "))
new_list = []
for i in list:
    if i != number:
        new_list = new_list + [i]

print("Original list =", list)
print("After removing =", new_list)