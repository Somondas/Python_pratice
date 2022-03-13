"""
8. Write a Python program to check a list is empty or not. Go to the editor
Click me to see the sample solution
"""

def check(lst):
    if len(lst) == 0:
        print("List is empty")
    else:
        print("List is not empty")

ls1= []
lst2 = [1.3,4,5,6,7,8,4]
check(ls1)
check(lst2)
