# Code to remove all duplicate values from a list and a tuple. 

def remove_dups(lst,tup):
    new_list = list(set(lst))
    new_tuple = list(set(tup))
    return new_list, new_tuple

iamlist= [1,23,4,5,6,7,23,0,5]
iamtuple= (1,23,4,5,6,7,23,0,5)

unique_list, unique_tuple = remove_dups(iamlist, iamtuple)

print('List without duplicates : ', unique_list)
print('Tuple without duplicates : ', unique_tuple)

