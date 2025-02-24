'''Write a  Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350'''

lst = [11, 33, 50]
lst = [str(i) for i in lst] 
lst.append("".join(lst)) 
print(int(lst[-1]))

# OR

def list_to_int(lst):
    return int("".join(map(str, lst)))

print(list_to_int([11, 33, 50]))
