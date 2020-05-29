import math

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node


class Solution:
    def partition(self, head: Node, x: int) -> Node:
        head_l1 = l1 = Node(-math.inf)
        head_l2 = l2 = Node(-math.inf)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        l2.next = None
        l1.next = head_l2.next
        return head_l1.next



