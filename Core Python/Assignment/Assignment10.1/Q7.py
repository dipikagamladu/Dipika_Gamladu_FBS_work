# WAP python to find the  intersection of two lists.
list1 = [10,20,30,40,50,]
list2 = [30,40,50,60,70]

intersection = []
for i in list1 :
    if i in list2:
        intersection.append(i)
print(intersection)