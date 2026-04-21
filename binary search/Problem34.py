"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def firstOccurance(nums, target):
            s = 0
            e = len(nums) - 1
            fc = -1

            while(s <= e):
                m = (s+e)//2
                if nums[m] == target:
                    fc = m
                    if m ==0 and nums[m - 1] != target:
                        return fc
                    else:
                        e = m - 1
                elif target > nums[m]:
                    s = m + 1
                else:
                    e = m - 1
            return fc
        
        def lastOccurance(nums, target):
            s = 0
            e = len(nums) - 1
            lc = -1

            while(s <= e):
                m = (s+e)//2
                if nums[m] == target:
                    lc = m
                    if m != len(nums) -1  and nums[m + 1] == target:
                        s = m + 1
                    else:
                        return lc
                elif target > nums[m]:
                    s = m + 1
                else:
                    e = m - 1
            return lc
        fc = firstOccurance(nums, target)
        lc = lastOccurance(nums, target)
        return [fc, lc]



