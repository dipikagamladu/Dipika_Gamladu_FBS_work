#write a program to input two angles from user and find third angle of the traingle.
angle1 = int(input('Enter first angle:'))
angle2 = int(input('Enter second angle:'))
angle3 = 180 - (angle1 + angle2)
print("Third angle of triangle = ",angle3)
