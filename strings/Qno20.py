"""
Write a Python function to reverses a string if it's length is a multiple of 4
"""

def reverse(text):
    new_str = ""
    if len(text) % 4 == 0:
        new_str = text[::-1]
        return new_str
    else:
        return text

print(reverse("12345678"))
print(reverse("1234"))
        
