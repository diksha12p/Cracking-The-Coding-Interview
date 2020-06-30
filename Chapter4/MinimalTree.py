from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minimalBST(arr: List[int]) -> TreeNode:
    return insert(arr, 0, len(arr) - 1)


def insert(arr: List[int], low: int, high: int) -> TreeNode:
    if low > high:
        return None
    mid = (low+high) // 2
    root = TreeNode(mid)

    root.left = insert(arr, low, mid - 1)
    root.right = insert(arr, mid + 1, high)

    return root


if __name__ == '__main__':
    print(minimalBST([-10,-3,0,5,9]))