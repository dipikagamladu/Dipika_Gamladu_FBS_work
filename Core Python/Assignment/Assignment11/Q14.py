#13. Python Program to count the occurrences of ach word in a string.

string = input("Enter a string: ")
words = string.split()
for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count = count + 1

    print(words[i], ":", count)
