# -*- coding: utf-8 -*-
"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
def swap(s1, s2):
    return f"{s2[:2] + s1[2:]} {s1[:2] + s2[2:]}"

result = swap('abc', 'xyz')
print(result, '\n')



'''OR'''

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
