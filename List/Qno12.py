"""
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

def remove_ele(lst):
    
   for item in lst:
       if lst.index(item) == 0 or lst.index(item) == 4 or lst.index(item) == 5:
            lst.remove(item)
   return lst

print(remove_ele(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
