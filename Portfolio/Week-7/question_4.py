'''
One approach to analysing some encrypted data where a substitution is suspected is frequency analysis. A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters. In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text.
Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so best to ignore that initially, and then check the usual resources for the runes.
'''
# This program displays the six most common letters in a message
lst=[]
message=input("Enter the message: ").lower()
mes=set(message.lower())
try:
    mes.remove(' ')
except:
    pass
def return_position(z):
    return z[1]
for x in mes:
    lst.append([x,message.count(x)])
lst.sort(key=return_position,reverse=True)
print("The top 6 most common letters in the message is: ")
for x in range(6):
    print(f"{lst[x][0]} : {lst[x][1]}")


