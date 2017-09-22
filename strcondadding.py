'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends
with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged '''

import time
str_1=str(input("Please enter a string :"))
print("Alalyzing ...")
time.sleep(1)
if str_1[-3:] == 'ing':
    print("As the word ends with ing,replacing it with ly ...")
    time.sleep(1)
    print(str_1[0:-3] + 'ly')
else:
    print("As the word doesn't end with ing , keeping it as it is ... ")
    print(str_1)