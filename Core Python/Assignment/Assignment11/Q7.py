#Python Program to Calculate the Length of a String Without Using a Library Function
string = input("Enter a string: ")
count = 0
for i in string:
    count = count + 1
print("Length of string:", count)