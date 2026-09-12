# Write a program to check if year is leap year or not.
def leap(year):
    if year % 4 ==0:
        return 'Leap year'
    else:
        return 'Not leap year'
year=int(input('Enter year:'))    
print(leap(year))       
