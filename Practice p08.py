'''Write a Python program to read a name from the user and print its abbreviated form.
Sample Input: ‘Sachin Ramesh Tendulkar’
Expected Output: 'SRT'
'''
full_name=input('Please enter the full name : ')
lst = full_name.split()
short_name = ""   # traverse in the list 
for i in range(len(lst)):
      full_name = lst[i]
      short_name += (full_name[0].upper()+'.')

print("Short Form of Name Is ::>",short_name) 