'''Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
in sorted form (alphanumerically) ?'''

import time


items=input("Please enter the comma separated words :")
word=[word for word in items.split(",")]
print(word)
print("Sorting the input ...")
time.sleep(1)
word.sort()
print(word)


