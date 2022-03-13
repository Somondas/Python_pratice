"""
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
Click me to see the sample solution
"""

def add_ing(word):
    new_word = word
    if len(word) < 3:
        return  new_word
    elif word[-3:] == "ing":
        new_word += "ly"
    else:
        new_word += "ing"

    return  new_word

print(add_ing("programm"))