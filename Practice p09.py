'''Q4.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already 
ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample Input: 'run'
Expected Output: 'runing'
Sample Input: : 'string'
Expected Output: : 'stringly'
'''
input_str=input('Enter a string : ')
if len(input_str)<3:
     print('Answer : ',input_str)
elif input_str.endswith('ing'):
     print('Answer : ',input_str + 'ly')
else:
     print('Answer : ',input_str + 'ing')
     