#write a program to convert days into years, weeks and days.
days = int(input('Enter number of days:')) 
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days = remaining_days % 7

print("years=",years)
print("weeks=",weeks)
print("days=",days)
