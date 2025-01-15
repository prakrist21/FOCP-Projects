'''
When processing data it is often useful to remove the last character from some input (it is often a newline). Write and test a function that takes a string parameter and returns it with the last character removed. (If the string contains one or fewer characters, return it unchanged.)
'''
def data(val):
    '''
    This function accepts a string and prints it by removing the last character.
    '''
    if len(val)>1:
        val=val[0:-1]
        print(val)
    else:
        print(val)

data('Computer')
