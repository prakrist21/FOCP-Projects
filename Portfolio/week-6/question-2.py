'''
Write and test a function that takes an integer as its parameter and returns the factors of that integer. (A factor is an integer which can be multiplied by another to yield the original).
'''
lst=[]
def factor(num):
    # This function prints the factor of the number.
    for x in range(1,num+1):
        if num % x == 0:
            lst.append(x)
    print(lst)

factor(24)