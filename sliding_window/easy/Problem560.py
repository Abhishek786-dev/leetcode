"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums, k):
        table = {0: 1}
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in table:
                count += table[prefix_sum - k]

            table[prefix_sum] = table.get(prefix_sum, 0) + 1
        return count


obj = Solution()
resp = obj.subarraySum([1, 2, 3], 3)
print(resp)
