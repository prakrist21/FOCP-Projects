'''
Write a program that takes the name of a file as a command-line argument, and creates a backup copy of that file. The backup should contain an exact copy of the contents of the original and should, obviously, have a different name.
'''
# This program creates an exact copy of the file you want.
import sys
f1=open(f'{sys.argv[1]}','r')
f2=open("copied.txt",'w')

data=f1.read()
f2.write(data)
