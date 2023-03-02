#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split(" ")[-1]
        return len(last_word)
# @lc code=end

