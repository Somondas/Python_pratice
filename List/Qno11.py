"""
11. Write a Python function that takes two lists and returns True if they have at least one common member.
"""

def check_common(n, m):
    common_list_elements = list(set(n).intersection(m))
    if len(common_list_elements)>0:
        return True
    else:
        return False



lst1 = [1,2,3,45,6,7,3]
lst2 = [1,5,4,5,6,7,8]
print(check_common(lst1, lst2))
