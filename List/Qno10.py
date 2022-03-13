"""
10. Write a Python program to find the list of words
that are longer than n from a given list of words.
"""

def filter_lst(n, text):
    new_lst = []
    txt = text.split(" ")
    for item in txt:
        if len(item) > n:
            new_lst.append(item)

    print(new_lst)



str1 = "I am a web-developer"
filter_lst(4, str1)
