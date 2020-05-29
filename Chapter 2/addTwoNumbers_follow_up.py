import math

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self,l1, l2):
        if not l1 and not l2:
            return None
        if not l1 and l2: return l2
        if not l2 and l1: return l1

        result_l1, result_l2 = 0, 0
        while l1 or l2:
            if l1:
                result_l1 = result_l1*10 + l1.val
                l1 = l1.next
            if l2:
                result_l2 = result_l2 * 10 + l2.val
                l2 = l2.next

        result = result_l1 + result_l2

        dummy_head = ListNode(-math.inf)
        curr_node = dummy_head
        for char in str(result):
            curr_node.next = ListNode(int(char))
            curr_node = curr_node.next

        return dummy_head.next







