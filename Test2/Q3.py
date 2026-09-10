# A farmer has a field which is half in circle share and rest rectangle.
#  He needs to do fencing for entire field using barbed wire 5 times.
#  Circular section has radius 20m and rectangle length is 50 m and breadth is 40m.
#  If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

import math
radius = 20
length = 50
breadth = 40
cost_per_meter = 35
times = 5

# Perimeter of circular section
circle_perimeter = 2 * math.pi * radius

# Perimeter of rectangular section
rectangle_perimeter = 2 * (length + breadth)

# Total fencing required
total_perimeter = circle_perimeter + rectangle_perimeter
total_wire = total_perimeter * times

# Total cost
total_cost = total_wire * cost_per_meter

print("Total length of wire required =", total_wire, "m")
print("Total cost of fencing = Rs.", round(total_cost, 2))
