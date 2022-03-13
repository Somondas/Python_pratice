"""
4. Write a Python program to get a string from a given string where all occurrences of
 its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
#first I have to find the first character of the string and put it in a variable
#then I have to replace the new char with $ but it will replace all the letters to $
#so I have to make a new string which will have the original letter and add with the updated remaining part
#then I have to return it

def replace_str(text):
    char = text[0]
    new_text = text.replace(char, "$")
    full_text = char + new_text[1:]
    return full_text


print(replace_str("restart"))