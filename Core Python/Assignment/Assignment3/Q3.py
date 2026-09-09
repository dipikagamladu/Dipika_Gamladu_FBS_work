#Write a program to inputs angle of traingles and check whether traingle is valid or not.
a=int(input('Enter first angle:'))
b=int(input('Enter second angle:'))
c=int(input('Enter third angle:'))
if(a>0)&(b>0)&(c>0):
   print('Traingle is valid.')
   a+b+c==180
else:
   print('Traingle is not valid.')  