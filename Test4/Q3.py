#Write a program to print following pattern.
print('*'*22)
for i in range(10):
    for j in range(10 - i):
        print(" ", end=" ")
    print("*")

print("*" * 22)
