'''
Write a Python program that will return true if the two
given integer values are equal or their sum or difference is 5.
'''

def cheaker(x, y):
    if x==y or abs(x-y)==5 or abs(x+y)== 5:
        return True
    else:
        return False

print(cheaker(10, 5))
print(cheaker(3, 2))
print(cheaker(7, 8))
