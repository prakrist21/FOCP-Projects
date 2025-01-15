'''
Write a program that, when run from the command line, reports how many arguments were provided. (Remember that the program name itself is not an argument).
'''
# This program prints the number of arguments
import sys
print(len(sys.argv[1:]))