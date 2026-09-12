data = range(1,20)
def palindrome(num):
    temp=num
    rev=0
    while temp>0:
         rem=temp % 10
         rev=rev * 10 + rem
         temp=temp // 10
    return  num==rev     
res = tuple(filter(palindrome,data))             
print(res)       