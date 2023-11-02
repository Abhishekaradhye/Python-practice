# -*- coding: utf-8 -*-
"""
Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
words = input("Enter comma-separated words: ").split(",")
print(", ".join(sorted(set(words))))
