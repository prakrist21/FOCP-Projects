'''
Write and test a function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string. So, if the string is cheese, the list returned should be ['c', 'e', 'h', 's'].
'''
def check(word):
    # This function takes a string and prints a sorted list of all unique letters in the string
    lst=list(set(word))
    print("The sorted list of strings is",sorted(lst))
word=input("Enter any string: ")
check(word)