#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_x =  str(x)[::-1]
        if str(x) == reverse_x:
            return True
        
        return False
# @lc code=end

