"""
11. Write a Python program to remove the characters
which have odd index values of a given string
"""
def replace_odd(text):
    new_text = ""
    for char in range(1, len(text), 2):
        new_text += text[char]
    return new_text



print(replace_odd("javascript"))