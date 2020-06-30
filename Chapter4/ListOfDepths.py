from typing import List
from collections import deque

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def binarytree_to_ll(root: TreeNode) -> List[ListNode]:
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        dummy = ListNode(0)
        curr_list_node = dummy
        size = len(queue)

        for i in range(size):
            curr_node = queue.popleft()
            curr_list_node.next = ListNode(curr_node.val)
            curr_list_node = curr_list_node.next

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.append(dummy.next)
    return result


def print_list(result : List):
    for entry in result:
        print(entry.val, ' -> ', end="")
        while entry.next:
            print(entry.next.val, ' -> ', end="")
            entry = entry.next
        print("None")


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(30)
    root.right = TreeNode(15)
    root.left.left = TreeNode(20)
    root.right.right = TreeNode(5)

    # print(binarytree_to_ll(root))
    print_list(binarytree_to_ll(root))



