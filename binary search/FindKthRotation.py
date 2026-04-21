"""
Given an increasing sorted rotated array arr[] of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr[] = [2, 4, 6, 9], if we rotate it by 2 times it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]

Examples:

Input: arr[] = [5, 1, 2, 3, 4]
Output: 1
Explanation: The given array is [5, 1, 2, 3, 4]. The original sorted array is [1, 2, 3, 4, 5]. We can see that the array was rotated 1 times to the right.
Input: arr = [1, 2, 3, 4, 5]
Output: 0
Explanation: The given array is not rotated.
"""


class Solution:
    def findKRotation(self, nums):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
        return start


# Driver code
if __name__ == "__main__":
    arr = [5, 1, 2, 3, 4]
    print(Solution().findKRotation(arr))
    arr = [1, 2, 3, 4, 5]
    print(Solution().findKRotation(arr))
