'''
Write and test a function that determines if a given integer is a prime number. A prime number is an integer greater than 1 that cannot be produced by multiplying two other integers.
'''
def prime(num):
    # This program checks if the 
    count=0
    for x in range(2,num//2 + 1):
        if num%x==0:
            count+=1
    if count>0:
        print("It is a composite number")
    else:
        print("It is a prime number")
prime(3)
