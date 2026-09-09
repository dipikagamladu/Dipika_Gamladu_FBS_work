# for i in range(1,5):
#     for j in range(1,i+1):
#          if j==1 or j==i:
#           print(1, end=' ')
#          else:
#           print(i-1,end=' ')
            
#     print()        
n = 4
for i in range(n):
    print(' ' *  (n - i),end=' ')
    num = 1

    for j in range(i+1):
        print(num, end=" ")
        num = num * (i-j) // (j+1)

    print()