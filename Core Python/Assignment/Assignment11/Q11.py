#11. Python Program to replace every blank space with hyphen in a string.

string = input("Enter a string: ")

new_string = ""

for i in string:
    if i == " ":
        new_string = new_string + "-"
    else:
        new_string = new_string + i

print("String after replacement:", new_string)