#Python Program to Check if a Given Key Exists in a Dictionary or Not
student = {
    "name": "Dipika",
    "age": 22,
    "city": "Pune"
}

key = input("Enter a key: ")

if key in student:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")