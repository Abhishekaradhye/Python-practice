'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length
is less than 2, return instead of the empty string.
Sample Input: 'Impetus'
Expected Output: 'Imus'
Sample Input: 'I'
Expected Output: Empty String
'''

input_str=input('Please enter the string : ')
if len(input_str)<2:
    print('String should be consisting of at least two alphabets. ')
else:
    
    print('Answer : ',input_str[:2]+input_str[-2:])
    
    
    
    