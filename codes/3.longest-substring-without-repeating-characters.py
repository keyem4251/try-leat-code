#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        d = dict()

        for c in s:
            if c not in d:
                d[c] = True
                longest = max(longest, len(d.keys()))
            else:
                longest = max(longest, len(d.keys()))
                d.clear()
                d[c] = True        

        return longest
# @lc code=end

