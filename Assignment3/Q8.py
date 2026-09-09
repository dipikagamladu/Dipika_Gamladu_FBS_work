#Write a program to prompt user to entere userid and password. After verifying userid and password display 
# a 4 digit random number and ask user to enter the same. If user enters the same number then show him
# success message otherwise failed. (something like captcha)


import random
username=(input('Enter username:'))
password=(input('Enter password:'))
if username == "Dipa" and password == "1234":
     number =random.randint(1000,9999)
     print("Your 4 digit number is :",number)
     user_number=int(input('Enter the same number:'))
     if(user_number==number):
        print("success")
     else:
        print("Failed")     
else:
     print("Invalid username or password")    