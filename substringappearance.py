'''Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows
the 'poor', replace the whole 'not'...'poor' substring with 'good' . Return the resulting string.?'''

import time
str_1=str(input("Please enter the string :"))
print("Calculating their indexes ...")
time.sleep(1)
print("not is found at",str_1.find('not'),"th place")
time.sleep(1)
x=str_1.find('poor')
print("poor is found at",str_1.find('poor'),"th place")

if str_1.find('not') < str_1.find('poor'):
    time.sleep(1)
    print("Replacing the substring from not...poor with good ...")
    time.sleep(1)
    final_string=str_1.replace(str_1[str_1.find('not'):],'good')
    print(final_string)
else:
    print("There is nothing to do in this case")

