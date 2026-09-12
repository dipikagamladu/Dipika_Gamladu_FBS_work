# Write a program to check if a given number is Armstrong or not. For each task create seperate functions.
def count_digit(n):
    count=0
    while n>0:
       count=count+1
       n=n // 10
    return count

def armstrong(n):
    digits=count_digit(n)
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**digits
        temp=temp // 10
    if sum ==n:
        return True
    else:
        return False
n=int(input('Enter number:'))
if armstrong(n):
    print('Armstrong number.')
else:
    print('Not Armstrong number.')