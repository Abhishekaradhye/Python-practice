def smallest_missing_integer(nums):
    # Sort the list
    nums.sort()
    # Initialize the smallest missing integer as 1
    smallest_missing = 1

    # Iterate through the sorted list
    for num in nums:
        # If the current number is equal to the smallest missing integer, increment it by 1
        if num == smallest_missing:
            smallest_missing += 1
        # If the current number is greater than the smallest missing integer, return it
        elif num > smallest_missing:
            return smallest_missing
    
    # If all numbers in the list are consecutive, return the next integer after the maximum number
    return smallest_missing

# Test cases
nums1 = [1, 0, 2]
nums2 = [5, 6, 8, 1]

print("Smallest missing integer in nums1:", smallest_missing_integer(nums1))  # Output: 3
print("Smallest missing integer in nums2:", smallest_missing_integer(nums2))  # Output: 2


