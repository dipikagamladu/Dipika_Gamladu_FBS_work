#Python program to remove the given key from dictionary.
dictionary = {"name": "Dipika", "age": 22, "city": "Pune"}

key = input("Enter key to remove: ")

if key in dictionary:
    del dictionary[key]
    print("Dictionary after removing key:", dictionary)
else:
    print("Key not found")