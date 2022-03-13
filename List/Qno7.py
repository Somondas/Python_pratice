"""
7. Write a Python program to remove duplicates from a list. Go to the editor
Click me to see the sample solution
"""



def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)

    return new_lst


print(remove_duplicates([1.2,3,4,5,5,5,1,2,3,3,3]))
