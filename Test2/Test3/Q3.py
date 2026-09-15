# Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then
#da = 10% ta = 12% and hra i = 15% otherwise la = 15%, 1 ta = 18% and hra-20%.
#  Based on this calculate the total salary of each emp and also total salary.

n = int(input("Enter number of employees: "))

total_all = 0
for i in range(1, n + 1):
    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100
    total = basic + da + ta + hra
    print("Employee", i)
    print("DA =", da)
    print("TA =", ta)
    print("HRA =", hra)
    print("Total Salary =", total)

    total_all = total_all + total
print("Total salary of all employees =", total_all)