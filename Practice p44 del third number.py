# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

def third_num(lst):
    target = 2
    while lst:
        if len(lst) < 3:
            target = len(lst) - 1
        removed_num = lst.pop(target)
        print('Removed: ', removed_num)
        
third_num([1,2,3,'Yes',55])
