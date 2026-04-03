"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

class Solution:
    def permute(self, nums):
        res = []
        n = len(nums)
        visited = [False] * n

        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                path.pop()
                visited[i] = False
        
        backtrack([])
        return res

# Example usage:
solution = Solution()
nums = [1, 2, 3]
result = solution.permute(nums)
print(result)
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Time complexity: O(n * n!) - There are n! permutations and generating each permutation takes O(n) time.
# Space complexity: O(n) - The space used by the recursion stack and the path list.