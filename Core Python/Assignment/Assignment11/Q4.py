#4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged.
string = input("Enter a string: ")

new_string = string[-1] + string[1:-1] + string[0]

print("New string:", new_string)