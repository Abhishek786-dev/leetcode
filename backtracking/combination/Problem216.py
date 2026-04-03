"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""

class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        start = 1

        def backtracking(start, path, remaining_sum):
            if len(path) == k and remaining_sum == 0:
                res.append(path[:])

            for i in range(start, 10):
                
                if i > remaining_sum:
                    break

                # include the current element and move to the next element
                path.append(i)
                
                # backtrack
                backtracking(i + 1, path, remaining_sum - i)
                # exclude the current element and move to the next element
                path.pop()


        backtracking(start, [], 0)
        return res

# Test cases
solution = Solution()
print(solution.combinationSum3(3, 7))
# Output: [[1, 2, 4]]
# Each element has 2 choices → include / exclude
# So, total combinations = 2^n where n is the number of elements in the input array.
# Time complexity: O(n * 2^n) where n is the number of elements in the input array. This is because there are 2^n subsets and generating each subset takes O(n) time.
# Space complexity: O(n) for the recursion stack and O(2^n) for the output list that contains all subsets.          
