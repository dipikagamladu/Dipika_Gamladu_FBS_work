#Input 5 subject marks from user and display grade (eg. First class , Second class...)

sub1 = int(input('Enter sub 1:'))
sub2 = int(input('Enter sub 2:'))
sub3 = int(input('Enter sub 3:'))
sub4 = int(input('Enter sub 4:'))
sub5 = int(input('Enter sub 5:'))

total = sub1+sub2+sub3+sub4+sub5 
percentage=total/5
print('total =',total)
print('percentage =',percentage)

if percentage>=95:
    print('Disticsion')
elif percentage>=60:
    print('First class')
elif percentage>=50:
    print('Second class')
elif percentage>=45:
    print('Pass')   
else:
    print('Failed')
          
    