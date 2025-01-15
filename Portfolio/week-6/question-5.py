'''
5. Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every fi h character, for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for clarity the random letters are not random:
send cheese
s  e  n  d   c  h  e  e  s  e
sxyexynxydxy cxyhxyexyexysxye

6. Write a program that decrypts messages encoded as above.
'''
import random
def check(word):
    # This function encrypts the given message.
    global encrp
    global space
    global spaceletter
    letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    space=random.randint(2,20)
    new=''
    spacew=' '*space
    for x in word:
        new=new+x+spacew
    print("The message with spaces:",new)
    spaceletter=''
    for x in range(space):
        new_letter=random.choice(letter)
        spaceletter=spaceletter+new_letter
    encrp=''
    for x in word:
        encrp=encrp+x+spaceletter
    print("The message after encryption:",encrp)

#Question 6 for decryption
word=input("Enter any word: ")   
check(word)
encrp=encrp.strip()
print("The message after decryption:",encrp[::space+1])