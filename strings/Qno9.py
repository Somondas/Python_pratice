"""
9. Write a Python program to remove the nth index character from a nonempty string.
"""


# TODO: Make a function block
def remove_str(text, n):
    new_str = text.replace(n, "")
    return  new_str

print(remove_str("Somon", "o"))
