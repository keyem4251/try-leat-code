#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
from collections import OrderedDict

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove_indexes = OrderedDict()

        for i, n in enumerate(nums):
            if n == val:
                remove_indexes[i] = True

        for i in reversed(remove_indexes.keys()):
            nums.pop(i)

        return len(nums)
# @lc code=end

