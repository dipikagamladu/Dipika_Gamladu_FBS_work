#WAP to print all number which are divisible by m and n in the list.

list = [10, 12, 15, 20, 30, 40, 60]
m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in list:
    if i % m == 0 and i % n == 0:
        print(i)