'''
Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you might also find one for the mean.
'''
def check(lst):
    '''
    This function takes a list as an arguement and prints its minimum, maximum and mean value.    
    '''
    print("The minimum temperture is",min(lst))
    print("The maximum temparature is",max(lst))
    print("The average temprature is",sum(lst)/len(lst))

lst=[]
for x in range(6):
    temp=input("Enter temprature: ")
    lst.append(float(temp))
check(lst)