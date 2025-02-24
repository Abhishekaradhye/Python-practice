'''Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]'''

def swap_adjacent(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

print(swap_adjacent([0, 1, 2, 3, 4, 5]))  # Works for any list length
print(swap_adjacent([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
