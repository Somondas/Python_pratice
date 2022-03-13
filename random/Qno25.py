#Write a Python program to check whether a specified value is contained in a group of values.

def is_here(group_data, n):
    for value in group_data:
        if n == value:
            return True
        
    return False
print(is_here([2,3,5,6],9))
