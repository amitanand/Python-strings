# Write a Python script that takes input from the user and displays that input back in upper and lower cases ?

import time


n=input("Do you want to enter in upper case (yes/no) :")
if n=='no':
    str_1=str(input("Please enter a string :"))
    print("Displaying the input in upper case ...")
    time.sleep(1)
    print(str_1.upper())
else:
    str_1 = str(input("Please enter a string :"))
    print("Displaying the input in lower case ...")
    time.sleep(1)
    print(str_1.lower())