#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i1 = 0
        i2 = 0

        for _ in range(m+n):
            n1 = None
            n2 = None

            print(f"result: {result}, i1: {i1}, i2: {i2}")
            if i1 < m:
                n1 = nums1[i1]
            if i2 < n:
                n2 = nums2[i2]

            if n2 is None or (n1 is not None and n1 < n2):
                result.append(n1)
                i1 += 1
            elif n1 is None or (n2 is not None and n1 >= n2):
                result.append(n2)
                i2 += 1
        
        for i, v in enumerate(result):
            nums1[i] = v
# @lc code=end

