#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        digit = 0
        for i in digits:
            digit += i * (10 ** n)
            n -= 1

        plus_one = digit + 1
        return [int(s) for s in list(str(plus_one))]

# @lc code=end

