"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums, target) :
        nums.sort()
        n = len(nums) - 1
        resultSum = 0
        minDiff = 2**31

        for i in range(n):
            left = i + 1
            right = n
            while(left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return target
                elif sum < target:
                    left += 1
                else:
                    right -= 1

                diffToTarget = abs(sum - target)
                if diffToTarget < minDiff:
                    resultSum = sum
                    minDiff = diffToTarget
        return resultSum

obj = Solution()
result=obj.threeSumClosest([1,1,1,0],100)
print(result)
