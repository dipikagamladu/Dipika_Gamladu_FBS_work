# Print 1 to 100 in snakes and ladder pattern.
num = 1
for row in range(1,11):
    if row % 2 == 1:
      for i in range(10):
         print(num,end=' ')
         num = num + 1
    else:
       start = num + 9
       for i in range(10):
          print(start,end=' ')
          start = start - 1
       num = num +10
    print()