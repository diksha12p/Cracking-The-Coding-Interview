class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete_at_pos(self, pos):
        if pos == 0:
            return
        if self.head is None:
            return

        dummy_head = Node(-1)
        dummy_head.next = self.head

        curr_node = dummy_head
        for _ in range(pos - 1):
            curr_node = curr_node.next
            if curr_node is None:
                break

        if curr_node is None:
            return

        if curr_node.next is None:
            return

        next_node = curr_node.next.next
        curr_node.next = None
        curr_node.next = next_node

    def printList(self):
        temp = self.head
        while (temp):
            print(" %d " % temp.value)
            temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List: ")
llist.printList()
llist.delete_at_pos(4)
print("\nLinked List after Deletion at position 4: ")
llist.printList()




