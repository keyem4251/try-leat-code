#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
from typing import Optional
from collections import OrderedDict

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = OrderedDict()

        node = head
        while node is not None:
            d[node.val] = True
            node = node.next

        result = None
        for key in reversed(d.keys()):
            node = ListNode(val=key)

            if result is None:
                result = node
            else:
                node.next = result
                result = node

        return result
# @lc code=end

