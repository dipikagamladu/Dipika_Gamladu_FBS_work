#Write a python program to find the two numbers of products is maximum among
#all the pairs in a given lists of numbers. use the python set
numbers = [2, 5, 3, 8, 4, 7]

num = set(numbers)

max_product = 0

for i in num:
    for j in num:
        if i != j:
            product = i * j

            if product > max_product:
                max_product = product
                n1 = i
                n2 = j

print("Two numbers are:", n1, "and", n2)
print("Maximum product:", max_product)