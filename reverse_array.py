"""
Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are [1, 4, 3, 2, 6, 5]. After reversing the array, the first element goes to the last position, 
the second element goes to the second last position and so on. Hence, the answer is [5, 6, 2, 3, 4, 1].
"""
class Solution:
    def reverseArray(self, arr):
        n = len(arr) - 1
        i = 0
        while(i<n):
            temp = arr[i]
            arr[i] = arr[n]
            arr[n] = temp
            i += 1
            n -= 1
        return arr

obj = Solution()
res = obj.reverseArray([1,2,3,4,5])
print(res)
