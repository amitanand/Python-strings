'''Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. Go to the editor
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

import time
def first_three(string):
    if len(string)<3:
        print("As length of the string is less than 3 , printing the same string ...")
        time.sleep(1)
        print("String :",string)
    else:
        print("As length of the string is greater than 3 , printing the last three char ...")
        time.sleep(1)
        print("Resulting string :",string[:3])
        time.sleep(1)

first_three('ipy')
first_three('Python')