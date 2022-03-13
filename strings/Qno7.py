"""
7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

# TODO: 1. I have to locate the substrings
def grammar(text):
    snot = text.find('not')
    spoor = text.find("poor")
    # TODO: 2. I have to set condition that if the not word comes before the poor
    #  string then only I have to replace the words with good

    if spoor > snot and spoor > 0 and snot > 0:
        text = text.replace(text[snot:spoor+4], "good")
        return text
    else:
        return text

print(grammar("The lyrics is not that poor! The lyrics is poor!"))