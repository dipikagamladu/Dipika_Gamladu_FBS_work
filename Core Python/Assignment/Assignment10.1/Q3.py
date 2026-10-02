#WAP to sort the list according to the second element in sublist.

list = [[1, 5], [2, 3], [4, 1], [3, 4]]
def second_element(x):
    return x[1]
list.sort(key=second_element)
print(list)