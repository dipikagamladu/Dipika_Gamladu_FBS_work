#1. To pass mulitiple parameter with meaning
#2. Mention 2 asterisk(**) symbol before para name function definition
#3. Passed data will be store in dictionary formate
#4. Use for loop to iterate values on dict.items.

def emp(**data):
    for key , val in data.items():
        print(key, ':', val)
emp(id=101, name='ABC', sal=40000, dept='IT')        