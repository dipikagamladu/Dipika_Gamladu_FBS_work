def strong(num):
    temp=num
    sum=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        fact=1
        for i in range(1,d+1):
            fact=fact*i
        sum=sum+fact
    if(sum==num):
         print(f'{num} is  a strong number.') 
    else:
        print(f'{num} is not a strong number.')    
num=int(input('Enter number:'))        
strong(num)     
