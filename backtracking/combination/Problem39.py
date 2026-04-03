"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        start = 0
        candidates.sort()

        def backtracking(start, path, remaining_sum):
            if remaining_sum == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining_sum:
                    break

                # include the current element and move to the next element
                path.append(candidates[i])
                # backtrack
                backtracking(i, path, remaining_sum - candidates[i])
                # exclude the current element and move to the next element
                path.pop()

        backtracking(start, [], target)
        return res
# Test cases
solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
# Output: [[2, 2, 3], [7]]
#  Each element has 2 choices → include / exclude
# So, total combinations = 2^n where n is the number of elements in the input array.
# Time complexity: O(n * 2^n) where n is the number of elements in the input array. This is because there are 2^n subsets and generating each subset takes O(n) time.
# Space complexity: O(n) for the recursion stack and O(2^n) for the output list that contains all subsets.
