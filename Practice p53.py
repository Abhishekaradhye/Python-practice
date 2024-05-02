# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

def to_int(lst):
    a = int(''.join(map(str,lst)))
    return a
print(to_int([11, 33, 50]),'\n\n')


# Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h


def missing_additional_values(list1, list2):
    missing_values = [x for x in list1 if x not in list2]
    additional_values = [x for x in list2 if x not in list1]
    
    return missing_values, additional_values

list1 = ['a', 'b', 'c','d']
list2 = ['b','d', 'c', 'g', 'h']

missing_values, additional_values = missing_additional_values(list1, list2)

print("Missing values in second list:", ','.join(missing_values))
print("Additional values in second list:", ','.join(additional_values))
