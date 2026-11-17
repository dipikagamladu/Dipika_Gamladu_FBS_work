#5. Python Program to Find the Union of two Lists without using set concept.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union = []
for i in list1:
    if i not in union:
        union.append(i)
for i in list2:
    if i not in union:
        union.append(i)
print("Union of the two lists is:", union)