#WAP to create three list of numbers, their squares and cubes.

list = [1, 2, 3, 4, 5]
squares = []
cubes = []
for i in list:
    square = i * i
    cube = i * i * i

    squares = squares + [square]
    cubes = cubes + [cube]

print("Numbers =", list)
print("Squares =", squares)
print("Cubes =", cubes)