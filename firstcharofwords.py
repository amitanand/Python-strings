''' Write a Python program to get a string from a given string where all occurrences of its first char
     have been changed to '$', except the first char itself  ?'''

import time
n=str(input("Please enter the string :"))
print("Changing all the occurrences of first char of the string to $ ...")
time.sleep(1)
str_1=n.replace(n[0],'$')
print(str_1)

