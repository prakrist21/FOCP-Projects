'''
Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).
'''
def covert_binary(num):
    # This function prints the number in binary number system.
    lst=[]
    while num!=0:
        rem=num%2
        lst.append(rem)
        num=num//2
    print(lst[::-1])

covert_binary(45)