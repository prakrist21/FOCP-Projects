'''
Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.
'''
# This program checks whether the entered URL works or not
import requests
import sys
try:
    url=sys.argv[1]
    response=requests.get(url)
    if len(sys.argv[:])==2:
        if response.status_code >=200 and response.status_code<404:
            print("It works")
        else:
            print('It doesnt works')
    else:
        print("Invalid, Multiple link sent")
except:
    print("This website doesnot exists")
