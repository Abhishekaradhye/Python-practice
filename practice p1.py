'''Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample Input: 'Impetus'
Expected Output: 'Imus'
Sample Input: 'I'
Expected Output: Empty String'''



input = input('Enter the string : ')

output = input[0:2]+input[-2:]

if len(input)<=2 :
    print('Please enter the valid string that contains minimum 3 charactors')
else:
    print(f'The string made of the first 2 and the last 2 characters is "{output}"')