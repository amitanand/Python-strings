'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string ?'''

import time

string_1=str(input("Please enter a string :"))
print("checking ...")
if len(string_1)<2:
    time.sleep(1)
    print("As the length of string is less than 2 ,printing the exact string :",string_1)
else:
    time.sleep(1)
    print("Printing the first 2 & last 2 char ...")
    time.sleep(1)
    print(string_1[0:2]+string_1[-2:])