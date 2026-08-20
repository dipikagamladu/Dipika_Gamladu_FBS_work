#write a program to reverse three digit number.
# a = 456
# print(f'Before_reversing a:{a}')
# p = a // 100
# q = a // 10 % 10
# r = a % 10
# a = r * 100 + r * 10 + p
# print(f'After_reversing a:{a}')


num = int(input('Enter three digit number:'))
a = num//100
b = num//10%10
c = num%10
reverse = c*100+b*10+a
print('reverse number=',reverse)