'''
Functions are often used to validate input. Write afunction that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise. Write a short program to test the function.
'''
def check(num):
    '''
    This function accepts integer value as argument and checks if it lies between 0-100.
    '''
    if num>=0 and num<=100:
        print("True")
    else:
        print('False')
check(101)
check(100)
check(99)
check(-10)
