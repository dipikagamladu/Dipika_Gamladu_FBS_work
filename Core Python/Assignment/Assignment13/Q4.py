#Write a program that finds all pairs of elements in a list whose sum is equal to a given value.
numbers = [2, 4, 3, 5, 7, 8, 1]
value = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == value:
            print(numbers[i], numbers[j])