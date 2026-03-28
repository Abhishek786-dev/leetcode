"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countF = defaultdict(int)
        i = 0
        j = 0
        max_len = 0

        while j < len(s):
            countF[s[j]] += 1
            while (j - i + 1) - max(countF.values()) > k:
                countF[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len


class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        d = {}

        replace = 0

        for i in s:
            d[i] = d.get(i, 0) + 1

            if d[i] > max_freq:
                max_freq = d[i]
            elif replace < k:
                replace += 1
            else:
                d[s[left]] -= 1
                left += 1

        return max_freq + replace


obj = Solution()
resp = obj.characterReplacement("AABABBA", 1)
print(resp)
