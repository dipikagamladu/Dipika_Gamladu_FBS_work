#Write a program to find a longest common prefix of all strings. use the python set
strings = ["flower", "flow", "flight"]

common = set(strings[0])

for string in strings[1:]:
    common = common.intersection(set(string))

prefix = ""

for char in strings[0]:
    if char in common:
        prefix = prefix + char
    else:
        break

print("Longest common prefix:", prefix)