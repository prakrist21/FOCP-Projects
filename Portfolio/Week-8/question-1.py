'''
The Unixnl command prints the lines of a text filewith a line number at the start of each line. (It can be useful when printing out programs for dry runs or white-box testing). Write an implementation of this command. It should take the name of the files as a command-line argument.
'''
# This program prints the line number at the start of each line.
f1=open("file1.txt",'r')
linecount=0
for x in f1.readlines():
    linecount+=1
    print(f"{linecount}. {x}")
