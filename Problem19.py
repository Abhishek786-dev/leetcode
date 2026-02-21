
"""
19. Remove Nth Node From End of List
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0)
        dummy.next = head
        first = head
        second = head

        for _ in range(n+1):
            first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

obj = Solution()
res = obj.removeNthFromEnd([1,2,3,4,5], 2)
print(res)