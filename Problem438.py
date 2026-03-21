"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []
        res = []

        target = [0] * 26
        window = [0] * 26

        for c in p:
            target[ord(c) - 97] += 1

        for i in range(len(s)):
            window[ord(s[i]) - 97] += 1

            if i >= len(p):
                window[ord(s[i - len(p)]) - 97] -= 1
            if target == window:
                res.append(i - len(p) + 1)
        return res
