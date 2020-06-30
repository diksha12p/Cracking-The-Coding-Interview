import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_height(root: Node):
    if not root:
        return 0
    return max(get_height(root.left), get_height(root.right))+1


def is_balanced(root : Node):
    if root is None:
        return True
    height_l = get_height(root.left)
    height_r = get_height(root.right)
    if abs(height_l - height_r) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    return False


def check_height(root: Node) -> int:
    if root is None:
        return 0
    h_left = check_height(root.left)
    if h_left == -sys.maxsize:
        return -sys.maxsize

    h_right = check_height(root.right)
    if h_right == -sys.maxsize:
        return -sys.maxsize

    if abs(h_left - h_right) > 1:
        return -sys.maxsize
    else:
        return max(h_right, h_left) + 1


def is_balanced_alt(root: Node):
    return check_height(root) != -sys.maxsize


if __name__ == '__main__':
    # root = Node(4)
    # root.left = Node(2)
    # root.left.left = Node(1)
    # root.left.right = Node(3)
    # root.right = Node(6)
    # root.right.left = Node(5)
    # root.right.right = Node(7)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    assert (is_balanced(root)) is True, " Not Balanced !! "
    assert (is_balanced_alt(root)) is True, " Not Balanced !! "
