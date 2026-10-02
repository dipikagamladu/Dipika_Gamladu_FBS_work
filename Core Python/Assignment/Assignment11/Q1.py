#Python Program to Replace all Occurrences of 'a' with $ in a String.
string = input("Enter a string: ")

new_string = ""

for i in string:
    if i == 'a':
        new_string = new_string + '$'
    else:
        new_string = new_string + i

print("New string:", new_string)