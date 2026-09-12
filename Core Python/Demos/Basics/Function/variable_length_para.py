#1. To pass multiple parameter to function
#2. Mention asterisk (*) symbol before parameter in function definition
#3. Values will be store in tuple formate
#4. Use for loop to iterates value from tuple.

def addition(*num):
    sum=0
    for val in num:
        sum+=val
    return sum    
res=addition(10,20,30,40,50) 
print(res)     