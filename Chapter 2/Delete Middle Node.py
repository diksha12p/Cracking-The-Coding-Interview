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

    def print_linked_list(self):
        if self.head is None:
            return ""

        node = self.head
        while node:
            print(node.value, end = "   ")
            node = node.next

    def delete_middle(self, node):
        curr_node = self.head
        while curr_node:
            if curr_node.value == node.value:
                curr_node.value = curr_node.next.value
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next


llist = LinkedList()
llist.push(6)
llist.push(7)
llist.push(1)
llist.push(4)
llist.push(4)
llist.push(8)
llist.print_linked_list()

print("\n")

middle_ele = Node(1)
llist.delete_middle(middle_ele)
llist.print_linked_list()
