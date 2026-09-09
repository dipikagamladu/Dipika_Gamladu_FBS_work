#Write a program to check if user has entered correct userid and password.
username=(input('Enter username:'))
password=(input('Enter password:'))
if username == "Dipa" and password == "1234":
    print("Login successfully.")
else:
    print("Invalid password.")    