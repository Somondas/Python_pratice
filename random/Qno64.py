"""
64. Write a Python program to get file creation
and modification date/times
"""
import os, time

print("Last modified: %s" % time.ctime(os.path.getmtime("Qno35.py")))
print("Created : %s" % time.ctime(os.path.getctime("Qno35.py")))
