# -*- coding: utf-8 -*-
"""
Write a Python program to create a Caesar encryption.

Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

"""

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

# Example usage
plaintext = "I am ready!"
shift = 3
encrypted_text = caesar_encrypt(plaintext, shift)

print(f"Plaintext: {plaintext}")
print(f"Encrypted text: {encrypted_text}")




