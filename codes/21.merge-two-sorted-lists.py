#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        item1 = None
        item2 = None

        if not list1 and not list2:
            return None

        while True:
            item1 = list1
            print(f"list1: {list1}")
            if list1 is None:
                break
            list1 = list1.next

            while True:
                item2 = list2
                print(f"list2: {list2}")
                if list2 is None:
                    break
                list2 = list2.next

        return result
# @lc code=end

