"""
60. Write a Python program to calculate the
hypotenuse of a right angled triangle
"""
from math import sqrt
print("Input the length of the sorter sides of the triangle:")
a=float(input("A: "))
b=float(input("B: "))
c = sqrt(a**2+b**2)
print("The length of the hypotenuse is", c)
