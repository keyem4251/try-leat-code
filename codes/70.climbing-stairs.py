#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        d = dict()
        d[0] = 1
        d[1] = 1
        if n in d:
            return d[n]
        
        key1 = n - 1
        key2 = n - 2
        i = 2

        while True:
            if key1 in d and key2 in d:
                return d[key1] + d[key2]

            d[i] = d[i-1] + d[i-2]
            i += 1
# @lc code=end

