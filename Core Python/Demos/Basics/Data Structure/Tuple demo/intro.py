#1. ()
#. tu = (10,)  #use comma for single value
tu = (10,20,30,'a',3.14,10)

#2. Heterogeneous

#3. Oredered

#4. Immutable

#5. Dup;icate elements allowed

# tu[0] = 50    #raise error

#6. Tuple is faster than list

import sys
li = []
tu = ()
print(type(tu))
print(tu)
print(sys.getsizeof(li))
print(sys.getsizeof(tu))