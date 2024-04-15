# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def are_all_unique(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return False  # Found a duplicate, return False
    return True  # No duplicates found, return True

# Example usage:
sequence1 = [1, 2, 3, 4, 5]
sequence2 = [1, 2, 3, 4, 4]

print(are_all_unique(sequence1))  # Output: True
print(are_all_unique(sequence2))  # Output: False
