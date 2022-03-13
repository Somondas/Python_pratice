Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(abs.__docstring__)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(abs.__docstring__)
AttributeError: 'builtin_function_or_method' object has no attribute '__docstring__'
>>> print(abs.__doc__)
Return the absolute value of the argument.
>>> 