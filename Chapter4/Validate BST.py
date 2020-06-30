class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Method 1: In order traversal with early cutoff
# Not using an array to compare at the end but a variable for simultaneous comparison
def is_valid(root: TreeNode) -> bool:
    # return bst_helper(root, [])
    return bst_helper(root, [0])


def bst_helper(root: TreeNode, prev = []) -> bool:
    if not root: return True

    if not bst_helper(root.left, prev):
        return False

    if prev and prev[0] >= root.val:
        return False
    prev[0] = root.val

    # if not prev:
    #     prev.append(root.val)
    # elif prev[0] >= root.val:
    #     return False
    #
    # prev[0] = root.val

    if not bst_helper(root.right, prev):
        return False
    return True


# Method 2: The Min/Max Solution - pass down min and max values as we iterate through the tree
def check_bst(root: TreeNode):
    return _min_max_solution(root, None, None)


def _min_max_solution(node: TreeNode, min, max):
    if node is None:
        return True

    if (max is not None and node.val > max) or (min is not None and node.val <= min):
        return False

    return _min_max_solution(node.left, min, node.val) and _min_max_solution(node.right, node.val, max)


if __name__ == '__main__':
    """
            7
           / \ 
          2   10
         / \
        1   5 
        
    """
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)

    assert is_valid(root) is True, "Not a BST "
    assert check_bst(root) is True, "Not a BST "

