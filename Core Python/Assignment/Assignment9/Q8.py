# WAP to check whether a number is prime or not using recursive.
def prime(n,i=2):
    if n<2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n,i+1)
n=int(input('Enter number:'))
if prime(n):
    print('Prime number.')
else:
    print('Not prime number.')    