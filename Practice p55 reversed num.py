# Given a signed 32-bit integer x, return x with its digits reversed.

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x = abs(x)
        else:
            negative = False
        rem = 0
        while x != 0:
            digit = x % 10
            rem = rem *10 +digit
            x //= 10
        if negative:
            rem = -rem
        return rem

ab = Solution()
print(ab.reverse(208))
print(ab.reverse(1467))
print(ab.reverse(50))

