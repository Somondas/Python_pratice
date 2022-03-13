"""
17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). Go to the editor
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""

def repeat_last(n):
    
    if len(n) < 2:
        return n
    else:
        new_str = ""
        count = 1
        while count <=4:
            new_str += n[-2:]
            count +=1
        return new_str


print(repeat_last("JavaScript"))
print(repeat_last("Python"))
