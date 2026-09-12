#1. pass    .. Neglect expected indentaition
# for i in range (1,10):
#     pass

#2.break      ...for terminating the loop.
# for i in range(1,10):
    # if(i==4):
    #     break
    # print(i)

#3. continue     ....To stop perticular iteration.
# for i in range(1,10):
#     if(i==4):
#         continue
#     print(i)

#4. else:         ....Will execute when loop executed successfully.
for i in range(1,10):
    if(i==4):
        continue
    print(i)
else:
    print('Enter block executed.')    

