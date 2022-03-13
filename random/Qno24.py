#Write a Python program to test whether a passed letter is a vowel or not.

def all_vowels(chr):
    all_vowels = "aeiou"


    return chr in all_vowels

x = str(input("Enter a letter: "))
print(all_vowels(x))
