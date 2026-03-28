"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub("[^a-zA-Z0-9]", "", s).lower()

        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True


obj = Solution()
res = obj.isPalindrome("A man, a plan, a canal: Panama")
print(res)
