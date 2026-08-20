# write a program to enter P,T,R and calculate compound interest.
P = int(input('Enter number:'))
R = int(input('Enter interest:'))
T = int(input('Enter year:'))

sum = (P*R*T) / 100
sum = P*(1+R/100)**T-P
print(sum)