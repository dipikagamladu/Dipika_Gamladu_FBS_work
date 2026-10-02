#python program to find the second largest number in a list using bubble sort.

list = [10, 5, 20, 8, 15]
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print("Sorted list:", list)
print("Second largest:", list[-2])