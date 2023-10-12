'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', 
except the first char itself.
Sample Input: 'restart'
Expected Output: 'resta$t' 
'''

input=input('Enter a string : ')
char=input[0]
if input.count(char)>=2:
    str1=input.replace(char[0],'$')
    output_str=char+str1[1:]
    print(output_str)
else:
    print('The charactor is not repeated')


