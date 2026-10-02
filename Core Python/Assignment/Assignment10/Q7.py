#7. Write a program to create a new list 
# from existing list which contains cube of each number of list.
list = [1, 2, 3, 4, 5]
cubes = []
for i in list:
    cube = i * i * i
    cubes = cubes + [cube]

print("Original list =", list)
print("Cube list =", cubes)