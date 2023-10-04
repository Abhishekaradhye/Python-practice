'''Write a program that accepts a string from user and redisplays the same string after removing vowels from it.'''


input_str=input('Please enter a string : ')
vowels='AEIOUaeiou'
new_str=''
for char in input_str:
    if char in vowels :
        pass
    else:
        new_str = new_str + char
print('String without vowels : ',new_str )
    
    
    