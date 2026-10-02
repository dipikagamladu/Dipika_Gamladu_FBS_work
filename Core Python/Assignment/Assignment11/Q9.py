#9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
string = input("Enter a string: ")

characters = 0
words = 0

for i in string:
    characters = characters + 1

    if i == " ":
        words = words + 1

words = words + 1

print("Number of characters:", characters)
print("Number of words:", words)