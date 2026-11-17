#2. A teacher came to class with a large box tokhat has several coins. Each coin has a number printed on it.
#Before coming to class, she ensured that All the numbers occur an Even number of times. However, while coming to the class,
# one coin fell down and got lost. She wants to find out the number on the missing coin.


n = int(input("Enter original number of coins: "))
coins = list(map(int, input("Enter coin numbers: ").split()))
for i in coins:
    count = coins.count(i)
    if count % 2 != 0:
        print("Missing coin number is:", i)
        break
