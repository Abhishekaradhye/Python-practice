# Write a  Python program to find items starting with a specific character from a list.

the_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
the_char = 'ab'
the_output =[]

for char in the_list:
    if char.startswith(the_char):
        the_output.append(char)
print("The items in the list starting with",the_char,":\n",the_output,'\n')



# Write a  Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.

lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    
result = [lst[0]]  # Initialize result list with the first element of the input list
for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:  # If current element is different from the previous one
        result.append(lst[i])  # Append it to the result list
    
print("List after removing consecutive duplicates",result)


# Write a Python program to calculate the hypotenuse of a right angled triangle.
from math import sqrt
def hypotenuse(base, height):
    return "{:.2f}".format(sqrt(base**2 + height**2))
print("\nHypotenuse of given right angles triangle is : ",hypotenuse(9, 13),'cm')