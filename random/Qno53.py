"""
53. Write a python program to access environment variables.
"""

import os

print("--------------------------------VARIABLES-----------------------------")
print(os.environ)
print("-----------------------------------HOME-------------------------------")
print(os.environ['HOME'])
print("-----------------------------------PATH-------------------------------")
print(os.environ['PATH'])
