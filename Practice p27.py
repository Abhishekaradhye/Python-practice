# -*- coding: utf-8 -*-
"""
Write a Python function to get a string made of 4 copies of the last two characters of a specified string
 (length must be at least 2).
"""

def four(text):
    return(text[:-2]+(text[-2:]*4))
print(four('Batman'))