
""""""
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums) - 1
        result = []
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                if j  > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j+1
                right = n
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum > target:
                        right -=1
                    elif sum < target:
                        left += 1
                    else:
                        result.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        right -=1
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left +=1
                        while left < right and nums[right] == nums[right+1]:
                            right -=1
        return result

obj = Solution()
res = obj.fourSum([1,0,-1,0,-2,2], 0)
print(res)