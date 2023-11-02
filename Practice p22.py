#Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def count_characters(s):
    return {char: s.count(char) for char in s}

result = count_characters('google.com')
print(result)
