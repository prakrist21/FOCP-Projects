'''
Modify your greeting program so that if the user does not enter a name (i.e. they just press enter), the program responds "Hello, Stranger!". Otherwise it should print a greeting with their name as before.
'''
#This program prompts the name of the user, and prints Hello, name. If the name is empty then it will display Hello Stanger!
name=input("Enter a name: ")
if name == '': 
    print("Hello Stranger!")
else:
    print(f"Hello {name}!")