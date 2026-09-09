# WAP TO PRINT ALL THE INTEGERS UPTO  N THAT ARE'NT DIVISIBLE BY 2 OR 3
num=int(input('Enter number:'))
for i in range(1,num+1):
     if i%2!=0 and i%3!=0:
        print(i)