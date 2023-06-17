#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        trimed_s = s.lstrip(" ")
        
        result_s = ""
        signs = ""

        if not trimed_s:
            return 0
        
        if trimed_s[0] in ("-", "+"):
            signs = trimed_s[0]
            trimed_s = trimed_s[1:]

        for c in trimed_s:
            if c.isdigit():
                result_s += c
            else:
                break

        if not result_s:
            return 0
        
        try:
            result = int(signs+result_s)
        except ValueError as e:
            return 0

        if result < (-2**31):
            return -2**31
        elif result > (2**31 - 1):
            return 2**31 - 1
        else:
            return result
# @lc code=end

