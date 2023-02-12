#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict()
        d["I"] = 1
        d["V"] = 5
        d["X"] = 10
        d["L"] = 50
        d["C"] = 100
        d["D"] = 500
        d["M"] = 1000

        result = 0

        for i, v in enumerate(s):
            if v == "I" and (len(s) > (i+1)) and s[i+1] in ["V", "X"]:
                result -= 1
            elif v == "X" and (len(s) > (i+1)) and s[i+1] in ["L", "C"]:
                result -= 10
            elif v == "C" and (len(s) > (i+1)) and s[i+1] in ["D", "M"]:
                result -= 100
            else:
                result += d[v]

        return result
# @lc code=end

