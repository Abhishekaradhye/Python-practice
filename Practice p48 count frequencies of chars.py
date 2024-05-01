# Write a Python program to get the frequency of elements in a list.

def frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

the_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequencies = frequency(the_list)

for item, count in frequencies.items():
    print(item, ":", count)
            


