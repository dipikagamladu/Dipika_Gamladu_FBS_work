# Write a program to calculate the total cost of painting. 
# The interior of building with four equal sized walls.

length = int(input("Enter the length of the wall (in m): "))
height = int(input("Enter the height of the wall (in m): "))
rate = int(input("Enter the painting cost :  "))

area = 4 * length * height

total_cost = area * rate

print("Area of four walls =", area, "sq.m")
print("Total cost of painting = Rs.", total_cost)
