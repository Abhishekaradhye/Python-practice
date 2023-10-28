# map function
def square(n):
    return n**2
l1 = [1,2,9,7,5]
sq = list(map(square,l1))
print('Squares of given numbers :',sq)

# filter function
def odd(m):
    if m % 2 != 0:
        return True
    else:
        return False
l2 = [1,2,9,7,5,100,54,56,55]
odd_numbers = list(filter(odd,l2))
print('Odd numbers : ',odd_numbers)

# reduce function
from functools import reduce
def addition(a,b):
    return a+b
l3 = [1,3,8,0,7]
total_sum = reduce(addition,l3)
print('Total sum of given numbers : ',total_sum)