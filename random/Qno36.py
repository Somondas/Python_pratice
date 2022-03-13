"""
Write a Python program to add two objects if both objects are an integer type.
"""

def add_number(x,y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Value must be integer check the fucking code.")
    return x+y
print(add_number(2, 2.59999999))
