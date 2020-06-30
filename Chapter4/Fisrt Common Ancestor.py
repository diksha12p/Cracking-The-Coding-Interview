class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def first_common_ancestor(root: TreeNode, p : int, q: int) -> TreeNode:
    if root is None:
        return TreeNode(None)
    if root.val == p or root.val == q:
        return root

    left_fca = first_common_ancestor(root.left, p, q)
    right_fca = first_common_ancestor(root.right, p, q)

    if left_fca and right_fca:
        return root
    return left_fca if left_fca else right_fca


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(30)
    root.right = TreeNode(15)
    root.left.left = TreeNode(20)
    root.right.right = TreeNode(5)

    tree = TreeNode(20)
    tree.left = TreeNode(10)
    tree.right = TreeNode(30)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(15)
    tree.left.left.left = TreeNode(3)
    tree.left.left.right = TreeNode(7)
    tree.left.right.right = TreeNode(17)

    print(first_common_ancestor(root, 15, 5).val)
    print(first_common_ancestor(tree, 10, 17).val)