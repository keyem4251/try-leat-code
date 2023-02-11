#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse_dict = {}
        for i_index, i in enumerate(nums):
            j = target - i
            if j in reverse_dict:
                return [reverse_dict[j], i_index]

            if i not in reverse_dict:
                reverse_dict[i] = i_index

   
# @lc code=end

