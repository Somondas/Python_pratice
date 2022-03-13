"""
Write a Python function to create the
HTML string with tags around the word(s). 
"""


def html_generator(letter, word):
    return f"<{letter}>{word}</{letter}>"

print(html_generator("html", "incognito"))
