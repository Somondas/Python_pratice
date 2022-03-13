'''
95. Write a Python program to check whether a string is numeric.
'''




strs = "12"

try:
    i =float(str)
except(ValueError, TypeError):
    print("\nNot numeric")
print()
