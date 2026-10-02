tu = (10,20,30,10)
#print(tu.count(10))
print(tu.index(30))

#add the element in tuple
tu_list = list(tu)
tu_list.append(40)
tu = tuple(tu_list)
print(tu)