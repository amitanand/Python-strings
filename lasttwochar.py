'''Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). Go to the editor
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses'''

import time
def string_two_char(string):
    print("Analyzing the last two char of the string :")
    time.sleep(1)
    two_char=string[-2:]
    result=two_char*4
    print("Preparing a string with 4 copies of the last two char ...")
    time.sleep(1)
    print("Resulting string :",result)

string_two_char('Python')
string_two_char('Excercises')