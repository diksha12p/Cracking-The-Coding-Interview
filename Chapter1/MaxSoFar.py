# import math
#
# def maxSubArray(nums):
#     max_so_far = -math.inf
#     max_ending_here = 0
#     size = len(nums)
#     for i in range(0, size):
#         max_ending_here = max_ending_here + nums[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
#
#         if max_ending_here < 0:
#             max_ending_here = 0
#     return max_so_far
#
#
# arr = [-1]
# print(maxSubArray(arr))
#
#
# # def moveZeroes(nums):
# #     """
# #     Do not return anything, modify nums in-place instead.
# #     """
# #     count = 0  # Count of non-zero elements
# #
# #     for i in range(len(nums)):
# #         if nums[i] != 0:
# #             # here count is incremented
# #             nums[count] = nums[i]
# #             count += 1
# #
# #     while count < len(nums):
# #         nums[count] = 0
# #         count += 1
#
#
#
#
# # def contiguous_arrays(arr):
# #     for i in range(len(arr)):
# #         for j in range(i+1, len(arr) + 1):
# #             print(arr[i:j])
# #
# #
# # arr = [1,2,4,5,1]
# # print(contiguous_arrays(arr))

from collections import Counter


def find_anagrams(s, p):
    k = len(p)
    d1 = Counter(p)
    result = list()
    substr = s[:k]
    d2 = Counter(substr)

    if d1 == d2:
        result.append(0)
    for i in range(len(s) - k):
        # Removing the current element
        if d2[s[i]] == 1:
            del d2[s[i]]
        elif d2[s[i]] > 1:
            d2[s[i]] -= 1

        # Adding the next element
        if s[k + i] in d2:
            d2[s[k + i]] += 1
        else:
            d2[s[k + i]] = 1

        if d1 == d2:
            result.append(i+1)
    return result


def group_anagrams(strs):
    result = list()
    for i in range(len(strs)):
        d1 = Counter(strs[i])
        for j in range(i+1, len(strs)):
            d2 = Counter(strs[j])
            if d1 == d2:
                result.append([strs[i], strs[j]])
    return result

s = "BACDGABCDA"
p = "ABCD"
# print(find_anagrams(s, p))

str = ["eat","tea","tan","ate","nat","bat"]
print(sorted(str))
print(group_anagrams(str))