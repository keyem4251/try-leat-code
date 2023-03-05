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
        n = len(digits) - 1 if digits[-1] != 9 else len(digits)
        result = []
        for i in range(len(digits)):
            result.append(int(plus_one / (10 ** n)))
            plus_one = plus_one % (10 ** n)
            n -= 1

        return result
# @lc code=end

