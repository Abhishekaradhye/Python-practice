#Write a program to reverse a string.(with and without using slicing)

str1=input('Enter a new string : ')

#with slicing
print('The reversed string : ',str1[::-1])

#without slicing
str0=' '
for i in str1:
    str0=i+str0
print('The reversed string : ',str0)
