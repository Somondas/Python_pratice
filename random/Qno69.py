"""
69. Write a Python program to sort three integers
without using conditional statements and loops.
"""

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z)-a1-a3


print("Numbers in sorted order: ",a1, a2, a3)
