'''
Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed the maximum, minimum, and mean. Create a version of that program that takes the values from the command-line instead. Be sure to handle the case where no arguments are provided!
'''
# This program prints the maximum , minimum and average temprature from the given arguement.
import sys
def check(lst):
    lst=[float(x) for x in lst]
    print("The minimum temperture is",min(lst))
    print("The maximum temparature is",max(lst))
    print("The average temprature is",sum(lst)/len(lst))

lst=[]
if len(sys.argv[:])>=2:
    lst=sys.argv[1:]
    check(lst)

else:
    print("Invalid, Arguments not enough")

