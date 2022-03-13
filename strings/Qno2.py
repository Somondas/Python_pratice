"""
Write a Python program to count the number of characters (character frequency) in a string
"""


def count_letters(text):
    result = {}
    for letter in text:
        if letter == " ":
            continue
        if letter not in result:
            result[letter] = 0
        result[letter] +=1
    return result

print(count_letters("I love to code!"))
