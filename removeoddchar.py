 #  Write a Python program to remove the characters which have odd index values of a given string. ?

import time

str_1=str(input("Please enter the string  :"))
print("Removing all the odd-char string ...")
time.sleep(1)
for i in range(len(str_1)):
    if (i%2== 0):
        print( str_1[i])
    else:
        pass


