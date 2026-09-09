#Write a program to check whether traingle is equilaterals , isosceles or scalene traingle.
a=int(input('Enter first side:'))
b=int(input('Enter second side:'))
c=int(input('Enter third side:'))
if(a==b)&(b==c):
   print("Equilaterals traingle.")
elif (a==b)or(b==c)or(a==c):
   print("Isosceles traingle.")
else:
   print("Scalen traingle.")  