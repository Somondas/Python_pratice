"""
62. Write a Python program to convert all units of time into seconds.
"""

days = int(input("Enter the number of days: ")) * 3600 * 24
hour = int(input("Enter the number of hours: ")) *3600
minutes = int(input("Enter the number of minutes: ")) * 60

time = days + hour + minutes
print("The amount of seconds: ",time)
