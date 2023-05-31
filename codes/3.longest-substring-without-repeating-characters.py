#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        d = dict()
        longest = 0
        checkout = dict()

        for i, c in enumerate(s):
            d[i] = list(c)

            for j in range(i):
                if c in d[j]:
                    checkout[j] = True
                elif j not in checkout:
                    d[j].append(c)

        for i, v in d.items():
            if longest < len(v):
                longest = len(v)
        
        return longest
# @lc code=end

