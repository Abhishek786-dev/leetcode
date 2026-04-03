"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

class Solution:
    def partition(self, s):
        res = []
        n = len(s)

        def backtrack(start, path):
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                substring = s[start:end+1]
                if not substring == substring[::-1]:  # Check if the substring is a palindrome
                    continue
                path.append(substring)
                backtrack(end+1, path)
                path.pop()


        backtrack(0, [])
        return res

# Example usage:
solution = Solution()
s = "aab"
result = solution.partition(s)
print(result)
# Output: [["a","a","b"],["aa","b"]]
# Time complexity: O(n * 2^n) - There are 2^(n-1) ways to partition the string and checking each partition takes O(n) time.
# Space complexity: O(n) - The space used by the recursion stack and the path list