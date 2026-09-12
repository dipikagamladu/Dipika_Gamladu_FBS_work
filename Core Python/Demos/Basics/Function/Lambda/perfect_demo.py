data = range(1,1000)
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum == num        
res = tuple(filter(perfect,data))             
print(res)       