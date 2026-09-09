# WAP TO FIND WHICH NUMBERS ARE DIVISIBLE BY 7 AND MULTIPLE OF 5 IN A GIVEN RANGE
start=int(input('Enter starting number:'))
end=int(input('Enter ending number:'))
for i in range(start,end+1):
    if(i % 7 == 0 and i % 5== 0):   
         print(i)
