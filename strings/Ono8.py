"""
8. Write a Python function that takes a list of words and return the longest word and the length of the longest one. Go to the editor
Sample Output:
Longest word: Exercises
Length of the longest word: 9
Click me to see the sample solution
"""

# TODO: 1. I have to find the longest string of the given list

def lon_str(text):
    lstr = max(text, key=len)
    nstr = len(lstr)
    print(f"The longest string is '{lstr}' and its length is {nstr}")

word_lst = ["Python", "JavaScript", "Go", "Java", "C"]
lon_str(word_lst)