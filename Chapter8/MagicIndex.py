# Find Magic Index in an array w/o duplicates
class MagicIndex:

    # Brute Force: Linear Search -> O(N)
    def find_magic_idx_linear(self, arr) -> int:
        for idx in range(len(arr)):
            if arr[idx] == idx:
                return idx
        return -1

    # Binary Search -> O(logN)
    def find_magic_idx_bs(self, arr) -> int:
        return self._helper_recursive(arr, 0, len(arr) - 1)

    # Iterative Implementation of Binary Search
    def _helper_iterative(self, arr, left, right) -> int:
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                return mid
            elif arr[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    # Recursive Implementation of Binary Search
    def _helper_recursive(self, arr, left, right):
        if right >= left:
            mid = (left + right) // 2
            if arr[mid] == mid:
                return mid
            elif arr[mid] > mid:
                return self._helper_recursive(arr, left, mid-1)
            else:
                return self._helper_recursive(arr, mid + 1, right)
        return -1


# Find Magic Index in an array WITH duplicates
class MagicIndexDup:
    def find_magic_idx(self, arr):
        return self._helper(arr, 0, len(arr)-1)

    def _helper(self, arr, left, right):
        if right >= left:
            mid = (left + right) // 2
            mid_val = arr[mid]
            if mid_val == mid:
                return mid

            # Instead of just searching on either the L or R side, we got to search on both, with a pruned search space
            # Left Search
            left_idx = min(mid-1, mid_val) # Trim down the search space
            left = self._helper(arr, left, left_idx)
            if left:
                return left

            # Right Search
            right_idx = max(mid + 1, mid_val)
            right = self._helper(arr, right_idx, right)
            return right


if __name__ == '__main__':
    magic = MagicIndex()
    print(magic.find_magic_idx_bs([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25]))
    print(magic.find_magic_idx_linear([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25]))

    magic_dup = MagicIndexDup()
    print(magic_dup.find_magic_idx([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))




