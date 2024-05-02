# Write a Python program to check whether a list contains a sublist.

def is_sublist(l,s):
    subset = False
    if s == []:
        subset = True
    elif s == l:
        subset = True
    elif len(s) > len(l):
        subset = False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                a = 1
                while (a < len(s)) and l[i+a] == s[a]:
                    a += 1
                if a == len(s):
                    subset = True
    return subset 

print(is_sublist([2, 4, 3, 5, 7], [4,3]))
print(is_sublist([2, 4, 3, 5, 7], [3,7]))
 

