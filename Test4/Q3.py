#Write a program to print following pattern.

for i in range(12):
    if i == 0:
        print("*" * 22)
    elif i == 11:
        print("*" * 22)
    else:
        print(" " * (22 - i * 2) + "*")
