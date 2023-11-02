# -*- coding: utf-8 -*-
"""
Write a Python function to convert a given string to all uppercase 
if it contains at least 2 uppercase characters in the first 4 characters.
"""
def convert(s):
    return s.upper() if sum(1 for char in s[:4] if char.isupper()) >= 2 else s

print(convert('Laptop'))
print(convert('Mr.Bean'))
print(convert('Virat Kohli'))

