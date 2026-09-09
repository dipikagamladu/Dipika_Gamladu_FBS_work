#Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3 times
#  After that program to terminate.

import random
attempts=0
logged_in=False
while attempts<3:
      username=(input('Enter username:'))
      password=(input('Enter password:'))
      if username == "Dipa" and password == "1234":
          logged_in=True
          break
      else:
          attempts+=1
          print("Incoorect username or password.")
          if attempts<3:
               print(f"{3-attempts} try (s)left.")
if logged_in:
          number=random.randint(1000,9999)
          print("Your 4 digit number is:",number)
          user_number = int(input('Enter the same number:'))
          if user_number==number:
                print("Password is correct.")   
          else:
                print("Password is incorrect.") 
else:
   print('You have used all 3 tries. Program terminated.')     