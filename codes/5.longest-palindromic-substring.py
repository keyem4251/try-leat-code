#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 1

        longest_substring = ""

        while left < len(s):
            # print(f"s[left:right]: {s[left:right]}, s[left:right][::-1]: {s[left:right][::-1]}, right: {right}, left: {left}")
            if len(longest_substring) >= len(s):
                break

            if s[left:right] == s[left:right][::-1] and len(longest_substring) < len(s[left:right]):
                longest_substring = s[left:right]

            right += 1
            if right > len(s):
                right = left
                left += 1

        return longest_substring

# @lc code=end

