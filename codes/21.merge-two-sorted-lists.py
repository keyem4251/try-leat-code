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
        temp = []

        if not list1 and not list2:
            return None

        while True:
            while True:
                if list2 is None:
                    break

                if list1 is None or list1.val >= list2.val:
                    temp.append(list2.val)
                    list2 = list2.next
                else:
                    break

            if list1 is None:
                break

            if list2 is None or list1.val <= list2.val:
                temp.append(list1.val)
                list1 = list1.next

        result = None
        for i in reversed(temp):
            node = ListNode(val=i)
            if result is None:
                result = node
            else:
                after = result
                node.next = after
                result = node

        return result
# @lc code=end

