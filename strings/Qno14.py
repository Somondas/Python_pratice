"""
14. Write a Python program that accepts a comma separated sequence of words as input and prints the
 unique words in sorted form (alphanumerically). Go to the editor
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
Click me to see the sample solution
"""

def sort_sentence():
    sentence = input("Enter the list of elements separated by commas: ")
    new_list = sentence.split(",")
    new_sen = [word for word in sentence.split(",")]
    print("".join(sorted(list(set(new_sen)))))



sort_sentence()



