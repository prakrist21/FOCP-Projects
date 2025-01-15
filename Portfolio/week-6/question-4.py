'''
Computers are commonly used in encryption. A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string. Write, and test, a function that takes a string containing a message and "encrypts" it in this way.
'''
def check(word):
    # This function removes all the space and reverses and prints the message
    word=word.replace(' ','')
    word=word[::-1]
    print(word)
check("   pr a kri s t")