# python program to count the frequency of words appearing in a string using a dictionary.
string = input("Enter a string: ")

words = string.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)