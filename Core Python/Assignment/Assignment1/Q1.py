#write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input('Enter number 1:'))
sub2 = int(input('Enter number 2:'))
sub3 = int(input('Enter number 3:'))
sub4 = int(input('Enter number 4:'))
sub5 = int(input('Enter number 5:'))

sum = sub1+sub2+sub3+sub4+sub5
print(sum)
percentage= sum/500*100
print(percentage)