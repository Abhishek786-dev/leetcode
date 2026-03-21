class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        r = 0
        b = len(nums) - 1
        while w <= b:
            if nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
        return nums


obj = Solution()
res = obj.sortColors([2, 0, 2, 1, 1, 0])
print(res)
