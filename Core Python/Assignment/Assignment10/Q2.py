# Write a program to find maximum number and minimum element in a list.
li = [40,50,30,60,20,10]
max = li[0]
min = 0
for ind in range(1,len(li)):
    if (li[ind] > max):
        min = max
        max = li[ind]     
    elif(li[ind]<min):
        min = li[ind]
print('maximum number =' ,max)     
print('minimum number =' ,min)                   
