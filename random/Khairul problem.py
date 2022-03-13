
#a = str(input("Enter ten Names: "))

#b = [a]
#print(f"Your names list is ready: {b}")

"""
Take ten names from the user and count and display the number at user who has
lenght more than 5 letter..
"""

a = str(input("Enter the first name:"))
b = str(input("Enter the second name:"))
c = str(input("Enter the third name:"))

d = (a, b, c)
for i in d:
    if len(i) == 5:
        print(i)
        print()
    else:
        continue
