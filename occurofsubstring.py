# Write a Python program to count occurrences of a substring in a string ?

import time

string_1=str(input("Please enter the string :"))
sub_string=str(input("Please enter the substring you want to count the occurrence of  :"))
print("Counting ...")
time.sleep(1)
occurrence = string_1.count(sub_string)
print(sub_string,"occured ",occurrence,"times")
