#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        
        for i, str_item in enumerate(strs):
            if i == 0:
                common_prefix = list(str_item)
                continue

            remove_index_list = []
            for i, c_p in enumerate(common_prefix):
                if (len(str_item) >= (i+1) and c_p != str_item[i]) or len(str_item) < (i+1):
                    remove_index_list.append(i)

            for remove_index in reversed(remove_index_list):
                common_prefix.pop(remove_index)

        return "".join(common_prefix)
            
# @lc code=end

