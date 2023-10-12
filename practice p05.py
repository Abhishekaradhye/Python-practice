#Write a Python program to remove the nth index character from a nonempty string.

i=input('Enter the string : ')
n=int(input('Enter the index number to be removed : '))

if len(i)<1:
    print('Pease enter some value')
else:
    first=i[:n]
    second=i[n+1:]
    output=first+second
    print(output)
    