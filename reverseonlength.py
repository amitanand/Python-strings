# Write a Python function to reverses a string if it's length is a multiple of 4 ?

import time

def revere_string(string):
    if len(string)%4 ==0:
        print(''.join(reversed(string)))
    else:
        pass

revere_string('abcdefghijkl')
revere_string('Adi')