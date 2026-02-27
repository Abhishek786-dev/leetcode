"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    """
    This class use for finding the length of the longest substring without repeating characters in a given string s. It uses a sliding window approach with two pointers (left and right) to keep track of the current substring being evaluated. A set is used to store the unique characters in the current substring. The algorithm iterates through the string, expanding the right pointer and adding characters to the set until a duplicate character is found. When a duplicate is encountered, the left pointer is moved forward, and characters are removed from the set until the duplicate character is removed. The maximum length of the substring is updated throughout the process.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])

        return maxLength
