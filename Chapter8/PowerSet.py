from typing import List


class PowerSet:
    # Approach 1: Recursive (DFS based)
    def subsets_recursive_dfs(self, nums: List[int]) -> List[List[int]]:
        result = []
        self._dfs(nums, 0, [], result)
        return result

    def _dfs(self, nums, curr_idx, path, result):
        result.append(path)
        for i in range(curr_idx, len(nums)):
            self._dfs(nums, i + 1, path + [nums[i]], result)

    @staticmethod
    # Approach 2: Iterative
    def subsets_iterative(nums: List[int]) -> List[List[int]]:
        result = [[]]
        for ele in nums:
            result += [subset + [ele] for subset in result]
        return result

    @staticmethod
    # Approach 3: Bit Manipulation
    def subsets_bit_manipulation(nums: List[int]) -> List[List[int]]:
        result = []
        # Iterating over all possible bit masks
        for bit_mask in range(1 << len(nums)):
            temp = []
            # Iterating over every index in nums
            for idx in range(len(nums)):
                # If the bit is set for 'idx' in 'bit_mask'
                if bit_mask & (1 << idx):
                    temp.append(nums[idx])
            result.append(temp)
        return result


if __name__ == '__main__':
    subsets = PowerSet()

    print(subsets.subsets_bit_manipulation([2,3,5,6]))
    print(subsets.subsets_iterative([2, 3, 5, 6]))
    print(subsets.subsets_recursive_dfs([2, 3, 5, 6]))
