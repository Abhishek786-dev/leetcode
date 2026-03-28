class Solution:
    def trap(self, height):
        count = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                count += left_max - height[left]
                left += 1
            else:
                count += right_max - height[right]
                right -= 1
        return count


obj = Solution()
res = obj.trap([4, 2, 0, 3, 2, 5])
print(res)

"""step 1: Initialize count to 0, left pointer to 0, right pointer to the last index of the height array, left_max and right_max to 0.
step 2: While left pointer is less than right pointer:
step 3: Update left_max to the maximum of left_max and height[left], and right_max to the maximum of right_max and height[right].
step 4: If left_max is less than right_max, add the difference between left_max and height[left] to count, and move the left pointer to the right by 1.
step 5: Otherwise, add the difference between right_max and height[right] to count, and move the right pointer to the left by 1.
step 6: Return count.

Time complexity: O(n), where n is the length of the height array. We traverse the array once.
Space complexity: O(1), as we are using only a constant amount of extra space.
"""
