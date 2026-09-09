#Write a program to inputs all sides of a traingle and check whether traingle is valid or not.
a=int(input('Enter first side:'))
b=int(input('Enter second side:'))
c=int(input('Enter third side:'))
if(a+b>c)&(b+c>a)&(c+a>c):
   print('Traingle is valid.')
else:
   print('Traingle is not valid.')  