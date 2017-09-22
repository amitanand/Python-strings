# Write a Python program to remove the last character from a nonempty string ?

import time
str_1=str(input("Please enter a string :"))
#n=int(input("Please enter the index no whose character you want to delete :"))
x=len(str_1)
print("deleting the character ...")
time.sleep(1)
print("Resulting string :",str_1[:x-1])