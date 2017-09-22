# Write a Python function that takes a list of words and returns the length of the longest one?

import time
list_1=[]
max_list=[]
i=0
n=int(input("Please enter the n of elements you want to put in the list :"))
while i<n:
    ele_list=input("Please enter the elemnt :")
    list_1.append(ele_list)
    i+=1
print("Preparing lists ...")
time.sleep(1)
print(list_1)

for i in list_1:
    max_list.append(len(i))
print("Calculating length of the elements of the list ...")
time.sleep(1)
print(max_list)
time.sleep(1)
print("Largest length :",max(max_list))