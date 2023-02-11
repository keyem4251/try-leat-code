#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums):
                if i_index != j_index:
                    if (i + j) == target:
                        return [i_index, j_index]

# @lc code=end

