'''Write a Python function to insert a string in the middle of a string. ?
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}} '''

import time

def string_to_enter(string,word):
    print("Combining a string in the middle of a string ...")
    time.sleep(1)
    print("Result :",string[:2] + word + string[2:])


string_to_enter('[[]]','Python')
string_to_enter('{{}}','PHP')