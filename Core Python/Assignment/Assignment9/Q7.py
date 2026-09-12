# WAP to find sum of digits using recursion.
def sum_digit(n):
    if n==0:
        return 0
    d = n % 10
    return d + sum_digit(n // 10)
n=int(input('Enter number:'))  
res=sum_digit(n)            
print(res)      