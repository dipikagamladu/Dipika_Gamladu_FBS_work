def armstrong(num):
    temp=num
    count=0
    while(temp>0):
        count+=1
        temp=temp//10
    temp=num
    sum=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        sum=sum+(d**count)
    if(sum==num):
        return(f'{num} is an armstrong number.')   
    else:
        return(f'{num} is not an armstrong number.')   
num=int(input('Enter number:'))         
print(armstrong(num))       
