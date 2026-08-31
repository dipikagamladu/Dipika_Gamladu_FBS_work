#write a program to accept distance in KM and convert in into meters and centimeters both.
km = float(input("Enter distance in KM: "))

meter = km * 1000
centimeter = km * 100000

print("Distance in meters =", meter)
print("Distance in centimeters =", centimeter)