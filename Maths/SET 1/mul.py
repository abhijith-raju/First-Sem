import numpy as num

list1=[]

list2=[]

di = input ("Enter dimension :")

var = int(di)

print('Enter the first  list element')

for i in range(var):

    mul = int(input())

    list1.append(mul)

print('Enter the 2nd  list element')

for j in range(var):

    mul = int(input())

    list2.append(mul)

li1 = num.array(list1)

li2 = num.array(list2)

list = li1*li2

print(list)