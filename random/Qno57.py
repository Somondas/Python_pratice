"""
57. Write a Python program to get execution time for a Python method.
"""
import time

def sum_of_num(n):
    start_time = time.time()
    a = 0
    for i in range(1, n+5):
        a = a +i
    end_time = time.time()
    return a, end_time-start_time

n =5
print("\n Time of the sum 1 to",n,"and required time to calculate the time:",
      sum_of_num(n))
