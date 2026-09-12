# Write a program to check if given number is Armstrong or not using recusive function.
def count_digit(n):
    if n==0:
        return 0
    return 1 + count_digit(n // 10)

def armstrong(n,digits,original):
    if n == 0:
        return 0
    digit=n%10
    return digit ** digits + armstrong(n //10,digits,original)
n=int(input('Enter number:'))
digits=count_digit(n)
res=armstrong(n,digits,n)

if res ==n:
    print('Armstrong number.')
else:
    print('Not Armstrong number.')