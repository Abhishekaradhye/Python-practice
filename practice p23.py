# -*- coding: utf-8 -*-
"""
Write a Python program to get a string from a given string 
where all occurrences of its first char have been changed to '$', 
except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
def repeated(s):
    return s[0] + s[1:].replace(s[0], '$')

result = repeated('restart')
print(result)
