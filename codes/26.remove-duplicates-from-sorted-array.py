#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
from copy import deepcopy

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count_d = dict()
        duplicated_indexes = []
        copied_nums = deepcopy(nums)

        for i, n in enumerate(nums):
            if n in count_d:
                duplicated_indexes.append(i)
            count_d[n] = True

        for i in reversed(duplicated_indexes):
            nums.pop(i)

        return len(count_d.keys())
# @lc code=end

