#program to find the Roots of a quadratic equation.
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

d=b**2-4*a*c
root1=(-b+d**0.5)/(2*a)
root2=(-b-d**0.5)/(2*a)

print('Root1=',root1)
print('Root2=',root2)