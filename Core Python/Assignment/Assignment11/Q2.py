#Python Program to Remove the nth Index Character from a Non-Empty String.
string = input("Enter a string: ")
n = int(input("Enter index to remove: "))

new_string = string[:n] + string[n+1:]

print("String after removing character:", new_string)