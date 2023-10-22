#Write a Python program to concatenate two strings in a third string. Do not use + operator.

str1=input('Enter the first string : ')
str2=input('Enter the second string :' )
str3=''.join([str1,str2])
print('The output string : ', str3)