"""
Linked List Data Structure:
    1. It is a linear data structure where each element is a separate object.
    2. Each element (node) of a list is comprising of two items - the data and a reference to the next node.
    3. The last node has a reference to null.
    4. The entry point into a linked list is called the head of the list.
    5. It is a dynamic data structure, which means that it can grow and shrink at runtime by allocating and deallocating memory.
    6. It is not a contiguous block of memory, which means that the elements are not stored in adjacent memory locations.
    7. It is a non-primitive data structure, which means that it is not a basic data type like int, float, char, etc.
    8. It is a collection of nodes that together represent a sequence.
    9. It is a data structure that can be used to implement other data structures like stacks, queues, etc.
    10 Insert at middle is easier than arrays because we don't have to shift elements to the right.
    11. Deletion at middle is easier than arrays because we don't have to shift elements to the left.
    12. It is a linear data structure, which means that it is a collection of nodes where each node is connected to the next node in the sequence.
    13. random access is not allowed in linked list, which means that we cannot access the elements of the list directly by their index. We have to traverse the list from the head to the desired index to access the element.
    14. Memory overhead is more in linked list than arrays because of the storage of additional pointer for each element.
Linked List Types:
    1. Singly Linked List:
        1. In a singly linked list, each node contains a reference to the next node in the list.
        2. It allows for traversal in only one direction, from the head to the tail of the list.
    2. Doubly Linked List:
        1. In a doubly linked list, each node contains a reference to both the next node and the previous node in the list.
        2. It allows for traversal in both directions, from the head to the tail and from the tail to the head of the list.
    3. Circular Linked List:
        1. In a circular linked list, the last node in the list points to the first node in the list.
        2. It can be either singly or doubly linked.
    4. Circular Doubly Linked List:
        1. In a circular doubly linked list, the first and last nodes in the list point to each other.
        2. It can be either singly or doubly linked.
        
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
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


obj = LinkedList()
obj.insert_at_beginning(10)
obj.insert_at_beginning(20)
obj.insert_at_beginning(30)
obj.insert_at_end(40)
obj.print_list()
print("\n Removing at beginning")
obj.remove_at_beginning()
obj.print_list()
print("\n Removing at end")
obj.remove_at_end()
obj.print_list()