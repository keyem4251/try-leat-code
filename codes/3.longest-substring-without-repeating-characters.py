#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        length = 0
        d = dict()

        for c in s:
            if c not in d:
                d[c] = True
                length += 1
            else:
                if longest < length:
                    longest = length
                length = 1
                d = {c: True}
        
        return longest if longest > length else length
# @lc code=end

