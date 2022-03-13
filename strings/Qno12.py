"""
12. Write a Python program to count the occurrences
of each word in a given sentence.
"""

# TODO: first I have to create a empty dictionary

def word_count(text):
    sen_list = text.split()
    count = {}
    for word in sen_list:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count

print(word_count("lorem ipsum lorem ipsum"))
