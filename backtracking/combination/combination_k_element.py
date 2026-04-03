"""
Given two integers n and k, return all possible combinations of k numbers chosen from 1 to n.
n = 4, k = 2

Expected output:

[
 [1,2], [1,3], [1,4],
 [2,3], [2,4],
 [3,4]
]
"""
class Solution:
    def combine(self, k:int, n:int):
        comb = []
        start = 1

        def backtracking(start, path):
            if len(path) == k:
                comb.append(path[:])
                return

            for i in range(start, n + 1):
                # include the current element and move to the next element
                path.append(i)
                # backtrack
                backtracking(i + 1, path)
                # exclude the current element and move to the next element
                path.pop()
        backtracking(start, [])
        return comb

# Test cases
solution = Solution()
print(solution.combine(2, 4))   
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# Each element has 2 choices → include / exclude
# So, total combinations = 2^n where n is the number of elements in the input array.
# Time complexity: O(n * 2^n) where n is the number of elements in the
# input array. This is because there are 2^n subsets and generating each subset takes O(n) time.
# Space complexity: O(n) for the recursion stack and O(2^n) for the output list that contains all subsets.
