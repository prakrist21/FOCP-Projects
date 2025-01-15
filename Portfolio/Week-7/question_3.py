'''
Write a program that manages a list of countries and their capital cities. It should prompt the user to enter the name of a country. If the program already "knows" the name of the capital city, it should display it. Otherwise it should ask the user to enter it. This should carry on until the user terminates the program (how this happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered variously as, for example, "Wales", "wales", "WALES" and so on.
'''
# This program prompts the user to enter the name of a country. If the program already "knows" the name of the capital city, it displays it. Otherwise it asks the user to enter it. This carry on until the user terminates the program.
dict={'nepal':'kathmandu','india':'new delhi','pakistan':'islamabad','egypt':'cairo','spain':'madrid','sri lanka':'colombo'}
while True:
    country=input("Enter the name of the country: ").lower()
    try:
        print(f"The capital city of {country} is {dict[country]}")
    except KeyError:
        capital_city=input(f"Sorry, I dont know the capital city of {country}. Please enter capital city of {country}: ")
        dict[country]=capital_city
    choice=input("Do you want to continue (Y/N): ").lower()
    if choice=='n':
        break