"""
 Write a Python program to print out a set containing all the colors
 from color_list_1 which are not present in color_list_2.
"""

color_list1 = set(['red','pink','blue'])
color_list2 = set(['black','pink','blue','green'])
print(color_list1.difference(color_list2))
