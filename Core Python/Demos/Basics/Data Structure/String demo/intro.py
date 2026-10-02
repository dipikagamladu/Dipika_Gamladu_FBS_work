#1. '', "", ''' ''', """ """
# str = 'Firstbit Solutions'
# str = "Firstbit Solutions"
# str = '''This is first line.
# THis is second line'''
# str = """This is first line.
# This is second line."""

#2. Set of characters (alpha,digits,symbols,space)

#3. Ordered (to maintain meaning of text)

#4. Immutable (faster execution)

#5. Duplicate character are allowed
# print(type(str))

#Reverse the string without using slicing
str = 'Firstbit Solutions'
rev = ''
for char in str:
    rev = char + rev
print(rev)