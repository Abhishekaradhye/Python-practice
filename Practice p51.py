#  Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']         n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

def conc(lst,n):
    lst1 = []

    for i in range (1, n+1):
        for item in lst:
            lst1.append(item+str(i))
    return lst1
print(conc(['p', 'q'], 5))


