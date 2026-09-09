for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(9 - 2 * i):
        print(' ',end=' ') 
    for j in range(4 if i == 5 else i, 0, -1):
         
                
         print(j,end=' ')
    print()       