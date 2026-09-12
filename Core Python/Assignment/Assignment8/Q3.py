#. Write a program to find sum of following series using functions:
#.a. 1+2+3+4+.....+n
#.b. 1!+2!+3!+4!+....n!
#.c. 1^1+2^2+3^3+.....n^n

#a...
def sum_series(n):
    sum=0
    for i in range(1, n + 1):
        sum=sum+i
    return sum
n = int(input('Enter n:'))
res=sum_series(n)
print('sum=',res)

#b...
def fact(n):
    sum=0
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        sum=sum + fact
    return sum
n=int(input('Enter n:'))
res=fact(n)
print('sum=',res)

#c...
def power(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i**i
    return sum
n=int(input('Enter n:'))
res=power(n)
print(res)