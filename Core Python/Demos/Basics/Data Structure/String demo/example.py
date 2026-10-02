# s1 = input('Enter first string: ')
# s2 = input('Enter second string: ')
# l1 = list(s1)
# l2 = list(s2)

# l1.sort()
# l2.sort()

# if l1 == l2:
#     print('Anagram')
# else:
#     print('Not Anagram')

s1 = 'aab'
s2 = 'baa'
l1 = list(s1)
l2 = list(s2)

l1.sort()
l2.sort()

if l1 == l2:
    print('Anagram')
else:
    print('Not Anagram')
