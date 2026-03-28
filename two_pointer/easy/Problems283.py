"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for k in range(1, len(nums)):
            if nums[i] == 0 and nums[k] != 0:
                temp = nums[i]
                nums[i] = nums[k]
                nums[k] = temp
                i += 1
            elif nums[i] != 0:
                i += 1

        return nums


obj = Solution()
res = obj.moveZeroes([1, 0, 1])
print(res)
