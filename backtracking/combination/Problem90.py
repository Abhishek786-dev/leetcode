"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsetsWithDup(self, nums):
        start = 0
        res = []
        nums.sort()

        def backtracking(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                #skip duplicates
                if i > start and nums[i] == nums[i -1]:
                    continue
                #include the current element and move to the next element        
                path.append(nums[i])
                #backtrack
                backtracking(i + 1, path)
                # exclude the current element and move to the next element
                path.pop()

        backtracking(start, [])
        return res

# Test cases
solution = Solution()
print(solution.subsetsWithDup([1, 2, 2]))
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Each element has 2 choices → include / exclude
# So, total combinations = 2^n where n is the number of elements in the input array.
# Time complexity: O(n * 2^n) where n is the number of elements in the input array. This is because there are 2^n subsets and generating each subset takes O(n) time.
# Space complexity: O(n) for the recursion stack and O(2^n) for the output list that contains all subsets.