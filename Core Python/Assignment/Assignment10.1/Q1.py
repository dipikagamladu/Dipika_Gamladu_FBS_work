#WAP to put even and odd elements of a list into two different list.
list = [10,15,20,25,30,35]
even = []
odd = []
for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)