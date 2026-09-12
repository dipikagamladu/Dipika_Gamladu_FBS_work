# WAP to print fibonacci series using recursion.
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+(n-2)
n=int(input('Enter number:')) 
for i in range(n):   
 print(fibonacci(i),end=' ')