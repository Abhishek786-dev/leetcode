"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsets(self, nums):
        start = 0
        res = []

        def backtrack(start, path):
            res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(start, [])
        return res

# Test cases
solution = Solution()
print(solution.subsets([1, 2, 3]))  
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#Each element has 2 choices → include / exclude
# So, total combinations = 2^n where n is the number of elements in the input array.
#Time complexity: O(n * 2^n) where n is the number of elements in the input array. This is because there are 2^n subsets and generating each subset takes O(n) time.
#Space complexity: O(n) for the recursion stack and O(2^n) for the output list that contains all subsets.
