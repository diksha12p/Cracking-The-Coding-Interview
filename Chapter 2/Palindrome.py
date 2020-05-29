class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Reaching the mid of the linked lsit
        fast , slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half i.e. from mid to the end
        prev = None
        while slow:
            next = slow.next
            slow.next = prev

            prev = slow
            slow = next

        # Comparing the first half and second half nodes respectively
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True



