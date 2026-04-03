"""
Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution:
    def permuteUnique(self, nums):
        res = []
        n = len(nums)
        visited = [False] * n
        nums.sort()  # Sort the array to handle duplicates

        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
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
nums = [1, 1, 2]
result = solution.permuteUnique(nums)
print(result)
#
# Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
# Time complexity: O(n * n!) - There are n! permutations and generating each permutation takes O(n) time.
# Space complexity: O(n) - The space used by the recursion stack and the path list.
"""
hink step-by-step

We have:

nums = [1,1,2]

At some recursion level, we are deciding whether to pick the second 1 (index i).

🔍 Case 1: not visited[i-1] ✅

👉 Means:

Previous duplicate (nums[i-1]) is NOT used in current path

So:

We are trying to pick the second '1' BEFORE picking the first '1'

➡️ This creates duplicate permutations ❌

👉 So we skip it

🔍 Case 2: visited[i-1] ❌

👉 Means:

Previous duplicate is already used in path

So:

We already picked first '1', now picking second '1'

➡️ This is valid ✅

Example:

[1,1,2]
🔥 Key insight

👉 We skip ONLY when:

same value + previous not used
🧠 One-line rule (remember this)

“If the previous duplicate hasn’t been used, skip the current one.”

❓ Why NOT use visited[i-1]?

If you used:

if nums[i] == nums[i-1] and visited[i-1]:

👉 You would skip valid cases like:

[1,1,2]
🔥 Visual intuition

Think of duplicates as:

1a, 1b

We allow:

1a → 1b ✅

We skip:

1b → 1a ❌ (same level duplicate)
"""