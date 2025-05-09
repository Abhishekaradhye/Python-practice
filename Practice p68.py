class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  
                if stack and stack[-1] == mapping[char]: 
                    stack.pop()  
                else:
                    return False  
            else:
                stack.append(char) 

        return len(stack) == 0  

# Test cases
print(Solution().isValid("()"))       # True
print(Solution().isValid("()[]{}"))   # True
print(Solution().isValid("(]"))       # False
print(Solution().isValid("([)]"))     # False
print(Solution().isValid("{[]}"))     # True
