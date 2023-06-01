#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        end = 0
        seen = set()

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                seen.remove(s[start])
                start += 1

        return max_len
# @lc code=end

