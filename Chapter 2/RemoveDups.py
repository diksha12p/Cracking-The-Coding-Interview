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

    def remove_dups(self):
        visited = set()

        current_node = self.head
        visited.add(current_node.value)
        while current_node.next:
            if current_node.next.value in visited:
                current_node.next = current_node.next.next
            else:
                visited.add(current_node.next.value)
                current_node = current_node.next
        return self.head


llist = LinkedList()
llist.push(6)
llist.push(7)
llist.push(1)
llist.push(4)
llist.push(4)
llist.push(8)
llist.print_linked_list()
print("\n")
llist.remove_dups()
llist.print_linked_list()