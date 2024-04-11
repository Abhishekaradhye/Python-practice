# Write a Python program to find all the pairs in a list 
#whose sum is equal to a given value.

def pairs_with_sum(lst, g_sum):
    complement_dict = {}
    pairs = []
      for num in lst:
        complement = g_sum - num
        if complement in complement_dict:
            pairs.append((num, complement))
        else:
            complement_dict[num] = complement
    return pairs

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 10

print("Original list:")
print(nums)

result = pairs_with_sum(nums, val)

print("List all pairs of the said list whose sum equals to", val)
print(result)

val = 35
print("\nOriginal list:")
print(nums)

result = pairs_with_sum(nums, val)

print("List all pairs of the said list whose sum equals to", val)
print(result)

val = 5

print("\nOriginal list:")
print(nums)

result = pairs_with_sum(nums, val)

print("List all pairs of the said list whose sum equals to", val)
print(result) 
