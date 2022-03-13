"""
10. Write a Python program to change a given string to
a new string where the first and last chars have been exchanged.
"""

# TODO: locate the first and the last char
def txt_replace(text):
    fchar = text[0]
    lchar = text[-1]
    new_txt = lchar + text[1:-1] + fchar
    return  new_txt

print(txt_replace("Python"))
print(txt_replace("lorem"))