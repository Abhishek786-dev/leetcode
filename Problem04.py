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

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         import pdb; pdb.set_trace()
#         if s==s[::-1]: 
#             return s
#         left = self.longestPalindrome(s[1:])
#         right = self.longestPalindrome(s[:-1])

#         if len(left)>len(right):
#             return left
#         else:
#             return right

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         longest = ''
        
#         def check(left, right):
#             while left >= 0 and right < n and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]
        
#         for i in range(n):
#             # Odd length palindromes
#             odd_palindrome = check(i, i)
#             if len(odd_palindrome) > len(longest):
#                 longest = odd_palindrome
            
#             # Even length palindromes
#             even_palindrome = check(i, i + 1)
#             if len(even_palindrome) > len(longest):
#                 longest = even_palindrome
        
#         return longest

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