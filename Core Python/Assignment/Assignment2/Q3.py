#convert distance given in feet and inches into meter and centimeter.
feet = int(input('Enter feet:'))
inches = int(input('Enter inches:'))
total_inches = feet * 12 + inches
centimeter = total_inches*2.54
meters = centimeter/100
print(total_inches)
print(centimeter)
print(meters)