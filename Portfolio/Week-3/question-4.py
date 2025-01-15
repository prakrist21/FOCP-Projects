'''
 Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus: BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
'''
# This program check if the entered password is in between 8-12 character and is in the list of common password or not.
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password=input("Enter a Password: ")
    password1=input("Enter Password again: ")
    if len(password)<=12 and len(password)>=8:
        if password not in BAD_PASSWORDS:
            break;

if password==password1:
    print("Password Set")
else:
    print("Error!The passwords doesnt match")