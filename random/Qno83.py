"""
83. Write a Python program to test whether
all numbers of a list is greater than a certain number
"""

nums = [4,5,2]

print()

print(all(x > 1 for x in nums))
print(all(x > 7 for x in nums))

print()
