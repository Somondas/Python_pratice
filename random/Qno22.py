'''
Write a Python program to count the number 4 in a given list
'''
def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count+=1
    return count

print(list_count([1,4,4,5,4,4,4,4,4,4]))
