# Enter number of students from user. for those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and average percentage of students.

num_students=int(input('Enter the number of students:'))
percentages=[]
for i in range(num_students):
    print(f'\nEnter marks for student{i+1}:')
    sub1 = int(input('Enter number 1:'))
    sub2 = int(input('Enter number 2:'))
    sub3 = int(input('Enter number 3:'))
    sub4 = int(input('Enter number 4:'))
    sub5 = int(input('Enter number 5:'))
    total = sub1+sub2+sub3+sub4+sub5
    percentage=(total/500)*100
    percentages.append(percentage)
print('/n--- Result ---')
for i in range(num_students):
    print(f'student {i+1} percentage: {percentages[i]:.2f}%')
average_percentage=sum(percentages)/num_students   
print(f'\nAverage percentage of all students:{average_percentage:.2f}%')