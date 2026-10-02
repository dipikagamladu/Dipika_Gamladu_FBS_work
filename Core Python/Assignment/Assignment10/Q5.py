# Accept a number from user and check if this element is present in the list or not.
# Also tell how many times it is present in the list.

list = [10, 20, 10, 30, 10, 40]
number = int(input("Enter a number: "))

count = 0

for i in list:
    if i == number:
        count = count + 1

if count == 0:
    print("Element is not present")
else:
    print("Element is present")
    print("It is present", count, "times")