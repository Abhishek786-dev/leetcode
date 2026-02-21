"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        n = self.head
        if n is None:
            print("List is empty")
        else:
            while n is not None:
                print(n.data, end=" --> ")
                n = n.next
    
    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    def remove_at_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
    
    def remove_at_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    
    def send_linked_list(self):
        return self.head

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print_head = dummy_head.next
        while print_head is not None:
            print(print_head.val, end=" --> ")
            print_head = print_head.next
        


l1 = LinkedList()
l2 = LinkedList()
l1.insert_at_end(2)
l1.insert_at_end(4)
l1.insert_at_end(3)
l2.insert_at_end(5)
l2.insert_at_end(6)
l2.insert_at_end(4)

obj = Solution()
obj.addTwoNumbers(l1.send_linked_list(), l2.send_linked_list())
