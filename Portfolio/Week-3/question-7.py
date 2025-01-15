'''
 Modify your "Times Table" program so that the user enters the number of the table they require. This number should be between 0 and 12 inclusive.
'''
# This program prints the table of number entered by the user.
num=int(input("Enter the number: "))
for x in range(13):
    print(f"{x} x {num} = {x*num}")