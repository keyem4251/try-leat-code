#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count_d = dict()
        
        for n in nums:
            count_d[n] = True

        return len(count_d.keys())
# @lc code=end

