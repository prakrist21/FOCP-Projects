'''
Modify the previous program so that it can process any numberof values. The input terminates when the user just pressed "Enter" at the prompt rather than entering a value.
'''
def check(lst):
    '''
    This function takes a list as an arguement and prints its minimum, maximum and mean value.    
    '''
    print("The minimum temperture is",min(lst))
    print("The maximum temparature is",max(lst))
    print("The average temprature is",sum(lst)/len(lst))

lst=[]
while True:
    num=input("Enter a number: ")
    if num=='':
        break
    lst.append(float(num))
check(lst)