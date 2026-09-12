# WAP to reverse a number using recursion.
def reverse(n,rev=0):
    if n ==0:
        return rev
    d=n%10
    rev= rev*10 +d
    return reverse(n//10,rev)
n=int(input('Enter number:'))   
res=reverse(n)
print(res)