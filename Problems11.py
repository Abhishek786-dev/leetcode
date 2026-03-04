"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

class Solution:
    def maxArea(self, height):
        L = 0
        R = len(height) - 1
        maxWater = []
        # H * W
        # H = min ()
        while(L<R):
            H = min(height[L], height[R])
            W = R-L
            maxWater.append(H*W)
            if height[L] > height[R]:
                R -=1
            else:
                L +=1
        return max(maxWater)
            
            
                    
                

obj = Solution()
res = obj.maxArea([8,7,2,1])
print(res)
