"""
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
Click me to see the sample
"""


lst = ["121", "abc", "545", "php", "go", "aba"]
count = 0
for item in lst:
    if len(item)>=2 and item[0] == item[-1]:
        count +=1

print(count)
