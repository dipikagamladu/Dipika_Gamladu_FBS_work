#9. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

numbers = [2, 4, 3, 5, 6, 7, 8]
target = 12

result = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                combination = (numbers[i], numbers[j], numbers[k])
                result.add(combination)

print("Unique combinations:", result)