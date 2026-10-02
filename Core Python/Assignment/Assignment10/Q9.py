#Write a program of having n number of elements in the list and find out 
# even and odd elements in that list and then create two separate lists which will have
#  even elements and other will have odd elements.

list = [10, 15, 20, 25, 30, 35]
even = []
odd = []

for i in list:
    if i % 2 == 0:
        even = even + [i]
    else:
        odd = odd + [i]

print("Even numbers =", even)
print("Odd numbers =", odd)