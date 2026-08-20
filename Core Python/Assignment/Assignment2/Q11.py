#write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input('Enter the amount:'))
n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

total = n500 + n200 + n100 + n50 + n20 + n10

print('total number of notes =',total)
