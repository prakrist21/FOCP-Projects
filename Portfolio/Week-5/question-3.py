'''
Write a program that takes a bunch of command-line arguments, and then prints out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them
'''
# This program prints the shortest from the given argument.
import sys
lst=sys.argv[1:]
lst_length=[]
for x in lst:
    lst_length.append(len(x))

print(lst[lst_length.index(min(lst_length))])