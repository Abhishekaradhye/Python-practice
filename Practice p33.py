def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
number = 5
fact = factorial(number)
print(fact)  # Output: 120
