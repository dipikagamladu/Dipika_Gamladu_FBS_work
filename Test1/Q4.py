#calculate the cost of painting the following bulding's wall (both interior and exterior). 
# you need to accept area(one wall) and the cost of both interior and exterior wall.

area = int(input("Enter area of one wall: "))
interior = int(input("Enter interior cost: "))
exterior = int(input("Enter exterior cost: "))

interior_cost = area * interior
exterior_cost = area * exterior

total_cost = interior_cost + exterior_cost

print("Interior painting cost =", interior_cost)
print("Exterior painting cost =", exterior_cost)
print("Total painting cost =", total_cost)
