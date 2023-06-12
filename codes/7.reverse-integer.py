#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if x < 0:
            reverse_str = "-" + str_x[1:][::-1]
        else:
            reverse_str = str_x[::-1]

        reverse_x = int(reverse_str)
        if (-2 ** 31) > reverse_x or (2 ** 31 -1) < reverse_x:
            return 0
        else:
            return reverse_x


# @lc code=end

