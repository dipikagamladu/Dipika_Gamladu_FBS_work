#. Sum of all prime numbers between 1 to n.
def prime(num):
    for i in range(1,num+1):
        if(num%i==0):
         print(i)
num =int(input('Enter number:'))         
prime(num)               