class Node:
    def __init__(self, val, parent = None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent


class Solution:
    def successor(self, root: Node, node: Node):
        if not root:
            return None
        if node.right:
            return self.lowest_in_right(node.right)
        else:
            curr = node
            q = node.parent
            while q and q.left != curr:
                curr = q
                q = q.parent
            return q

    def lowest_in_right(self, node : Node) -> Node:
        curr = node
        while curr:
            curr = curr.left
        return curr


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8, root)
    root.right = Node(22, root)
    root.left.left = Node(4, root.left)
    root.left.right = Node(12, root.left)
    root.left.right.left = Node(10, root.left.right)
    root.left.right.right = Node(14, root.left.right)

    sol = Solution()

    # assert sol.successor(root, root.left.right.right) == root
    # assert sol.successor(root, root.left.right.left) == root.left.right

    assert sol.successor(root, root.left.right.right).val == 20
    assert sol.successor(root, root.left.right.left).val == 12


