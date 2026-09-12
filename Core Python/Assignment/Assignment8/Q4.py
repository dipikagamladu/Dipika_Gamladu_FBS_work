# Sum of all odd numbers between 1 to n.
def odd(num):
    for i in range(1,num +1):
        if(i%2!=0):
         print(i)
num =int(input('Enter number:'))         
odd(num)               