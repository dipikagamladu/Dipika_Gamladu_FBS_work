data = range(1,1000)
def armstrong(num):
    temp=num
    sum=0
    while temp>0:
        rem=temp%10
        sum=sum+rem**3
        temp=temp//10
    return sum==num    
res = tuple(filter(armstrong,data))             
print(res)       