#program to find the area and perimeter of following figure (Accept the length , breadth and radius from user)
import math

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

area = l * b + (math.pi * r * r) / 2

perimeter = 2 * l + b + math.pi * r

print("Area =", area)
print("Perimeter =", perimeter)

