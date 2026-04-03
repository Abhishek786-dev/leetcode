"""
Given a string s, return all permutations of the string s in lexicographically sorted order.

Note: A permutation is the rearrangement of all the elements of a string.

Examples:

Input:  s = "ABC"
Output: "ABC", "ACB", "BAC", "BCA", "CAB", "CBA"

Input: s = "XY"
Output: "XY", "YX"

Input: s = "AAA"
Output: "AAA", "AAA", "AAA", "AAA", "AAA", "AAA"
"""


class Solution:
    def find_permutation(self, s):
        res = []
        s = sorted(s)

        def helper(index, s, path):
            if index == len(s):
                res.append(path)
                return

            for i in range(index, len(s)):
                # skip duplicates
                if i > index and s[i] == s[i - 1]:
                    continue
                # swap
                s[index], s[i] = s[i], s[index]
                helper(index + 1, s, path + s[index])
                # backtrack
                s[index], s[i] = s[i], s[index]

        helper(0, s, "")
        return res
