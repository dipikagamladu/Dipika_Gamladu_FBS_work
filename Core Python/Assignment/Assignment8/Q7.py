# Write a program to find sum of digits of a number
def sum_digit(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum    
n=int(input('Enter number:'))  
res=sum_digit(n)            
print(res)      