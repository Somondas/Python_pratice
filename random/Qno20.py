'''
Write a Python program to get a string which is n (non-negative integer) copies of a given string
'''
def larger_str(str,n):
    result = ""
    for i in range(n):
        result += str
    return result
print(larger_str("laka ", 5))
