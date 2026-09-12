data = range(1,20)
def prime(num):
    if num <2:
       return False
    for i in range(2,num):
        if num%i==0:
         return True       
res = tuple(filter(prime,data))             
print(res)       