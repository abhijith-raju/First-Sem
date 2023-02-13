import numpy as n

print("Enter vector1 :")

vect1 = [int(vect1) for vect1 in input().split()]

print("Enter the vector2 :")

vect2 = [int(vect2) for vect2 in input().split()]

div1 = n.array(vect1)

div2 = n.array(vect2)

div = div1//div2

print("Result = ",div)