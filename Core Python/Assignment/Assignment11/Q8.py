#Python Program to Remove the Characters of Odd Index Values in a String.
string = input("Enter a string: ")
new_string = ""
for i in range(len(string)):
    if i % 2 == 0:
        new_string = new_string + string[i]

print("String after removing odd index characters:", new_string)