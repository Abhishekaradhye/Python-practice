# Wite python code to Change the position of every n-th value with the (n+1)th in a list

def swap_eles(lst,n):
    print('Original  : ', lst)
    if n < len(lst)-1:
        for i in range(0, len(lst)-1, n):
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
print('Post Swap : ',swap_eles([0, 1, 2, 3, 4, 5], 2))

