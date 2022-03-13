"""
5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

# first I create two variables which contains the first char of the given strings


#second I have to swap the first char of the variable and to one another
# then I have to combine the two strings

def swap_str(word1, word2):
    new_word1 = word2[:2] + word1[2:]
    new_word2 = word1[:2] + word2[2:]
    new_str = new_word1 + " " + new_word2
    return  new_str

print(swap_str("abc", "xyz"))
