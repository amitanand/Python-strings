'''Write a Python program to get a single string from two given strings,separated by a space and swap
 the first two characters of each string '''

import time
str_1=str(input("Please enter the first string :"))
str_2=str(input("Please enter the second string : "))
print("Swapping the first 2 char with a space b/w it ...")
new_str1=str_1[0:2] + str_2[2:]
new_str2=str_2[0:2] + str_1[2:]
time.sleep(1)
print(new_str2+ "" +new_str1)