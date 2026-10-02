#Python Program to count number of digits and letters in a string.

string = input("Enter a string: ")
letters = 0
digits = 0

for i in string:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        letters = letters + 1
    elif i >= '0' and i <= '9':
        digits = digits + 1

print("Number of letters:", letters)
print("Number of digits:", digits)