#1. To neglect positional parameter concept
#2. Assign value to parameter in function call
#3. Name of parameter in function definition and function call should be same
#4. Flow from right to left(Why - positional parameter flow from left to right.)

def emp(id ,name,sal,dept):
    print('ID',id)
    print('NAME:',name)
    print('SALARY:',sal)
    print('DEPARTMENT:',dept)

emp(name='ABC',sal=20000,dept='IT',id=101)
