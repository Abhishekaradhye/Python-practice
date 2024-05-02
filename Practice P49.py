# Write a Python program to count the number of elements in a list within a specified range.

def elements_in_range(numbers, mini, maxi):
    if len(numbers) < 1:
        print('Blank List provided.')
    else:
        ranges = []
        for num in numbers:
            if mini<=num<=maxi:
                ranges.append(num)
        print("Number of elements in a list within the given range : ",len(ranges))

elements_in_range([],40, 100)
elements_in_range([10, 20, 30, 40, 40, 40, 70, 80, 99],40, 100)
elements_in_range(['a', 'b', 'c', 'd', 'e', 'f'],'a', 'e')