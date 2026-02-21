"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, string):
        n = len(string)
        for right in range(n, 0, -1):
            for left in range(n - right + 1):
                substring = string[left:left + right]
                print(f"left: {left}, right: {right}")
                print(f"substring: {substring}")
                if substring == substring[::-1]:
                    return substring
               
        
obj = Solution()
res = obj.longestPalindrome('babad')
print(res)