# write a program to find print the following fibonacci series using functions:
#  1 1 2 3 5 8 n terms
def fibonacci ():
      num=int(input('Enter number:'))
      a=-1
      b=1
      series=[]
      for i in range (num):
          series.append(a)  #append=add value in ending.
          c=a+b
          a=b
          b=c
      return series
res=fibonacci()
print(*res)