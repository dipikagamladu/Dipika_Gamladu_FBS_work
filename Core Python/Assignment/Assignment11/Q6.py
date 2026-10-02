#Python Program to Take in a String and Replace Every Blank Space with Hyphen
string = input("Enter a string: ")

new_string = ""

for i in string:
    if i == " ":
        new_string = new_string + "-"
    else:
        new_string = new_string + i

print("String after replacing spaces:", new_string)