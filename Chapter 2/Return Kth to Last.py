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

    def print_ll_from_node(self, node):
        while node:
            print(node.value, end = "   ")
            node = node.next


    def return_k_to_last(self,k):
        current_node, result = self.head, []
        for i in range(k):
            current_node = current_node.next

        while current_node:
            result.append(current_node.value)
            # print(current_node.value, end = " ")
            current_node = current_node.next
        return result

    def return_k_to_last_runner(self, k):
        runner, current_node = self.head, self.head
        for _ in range(k):
            if runner:
                runner = runner.next

        while runner:
            current_node = current_node.next
            runner = runner.next
        return current_node


llist = LinkedList()
llist.push(6)
llist.push(7)
llist.push(1)
llist.push(4)
llist.push(4)
llist.push(8)
llist.print_linked_list()

print("\n")

print(llist.return_k_to_last(3))


llist.print_ll_from_node(llist.return_k_to_last_runner(3))

