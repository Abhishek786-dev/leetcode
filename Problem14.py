"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        m_l = min(strs, key=len)
        res = ""
        for i in range(len(m_l)):
            chr = m_l[i]
            for el in strs:
                if el[i] == chr:
                    continue
                else:
                    return res
            res += chr
        return res
            
obj = Solution()
res = obj.longestCommonPrefix(["flower","flow","floight"])
print(res)
