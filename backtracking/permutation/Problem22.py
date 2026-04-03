"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(path, open_count, close_count):
            if len(path) == 2 * n:
                res.append(path)
                return
            if open_count < n:
                backtrack(path + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(path + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return res

# Example usage:
solution = Solution()
n = 3
result = solution.generateParenthesis(n)
print(result)
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Time complexity: O(4^n / sqrt(n)) - The number of valid parentheses combinations is given by the nth Catalan number, which is approximately 4^n / (n^(3/2)).
# Space complexity: O(n) - The space used by the recursion stack and the path string.