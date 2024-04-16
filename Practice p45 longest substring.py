'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
Example 1:

Input: s = "abcabcbb"               Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"                  Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"                 Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for a in range(len(s)):
            seen_eles = set()
            seen_length = 0

            for b in range(a, len(s)):
                if s[b] in seen_eles:
                    break
                seen_eles.add(s[b])
                seen_length += 1

            max_len = max(max_len,seen_length)
            
        return max_len
s1 = "accaabbcbb"
s2 = "bbbbb"
s3 = "pwwkew"
Solution = Solution()
print(Solution.lengthOfLongestSubstring(s1))
print(Solution.lengthOfLongestSubstring(s2))
print(Solution.lengthOfLongestSubstring(s3))