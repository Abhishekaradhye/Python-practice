# -*- coding: utf-8 -*-
"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""

def insert_string_middle(base_string, insert_string):
    return f"{base_string[:len(base_string)//2]}{insert_string}{base_string[len(base_string)//2:]}"

result1 = insert_string_middle('[[]]<<>>', 'Python')
result2 = insert_string_middle('{{}}', 'PHP')
r3 = insert_string_middle('Cricket', 'Football')

print(result1)
print(result2)
print(r3)
