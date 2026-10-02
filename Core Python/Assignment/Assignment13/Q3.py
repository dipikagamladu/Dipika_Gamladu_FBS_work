#3. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
strings = ["hello world", "hello python", "world python", "hello"]

words = set()

for string in strings:
    for word in string.split():
        words.add(word)

print("Unique words:", words)

for word in words:
    count = 0

    for string in strings:
        for w in string.split():
            if w == word:
                count = count + 1

    print(word, ":", count)