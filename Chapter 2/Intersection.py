class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr_A, curr_B = headA, headB
        len_A, len_B = 0, 0

        while curr_A:
            len_A += 1
            curr_A = curr_A.next

        while curr_B:
            len_B += 1
            curr_B = curr_B.next

        if curr_A is not curr_B:
            return False

        chop_off_threshold = abs(len_A - len_B)

        shorter_head = headA if len_A < len_B else headB
        longer_head = headB if len_B < len_A else headA

        for _ in range(chop_off_threshold):
            longer_head = longer_head.next

        while shorter_head is not longer_head:
            shorter_head = shorter_head.next
            longer_head = longer_head.next

        return longer_head




